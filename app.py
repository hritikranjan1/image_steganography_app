from flask import Flask, render_template, request, jsonify, send_file
import os
from PIL import Image
import stepic
from datetime import datetime

app = Flask(__name__)

# Define folders
UPLOAD_FOLDER = "static/uploads"
ENCODED_FOLDER = "static/encoded"

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCODED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode_image():
    if 'image' not in request.files or 'message' not in request.form:
        return jsonify({'error': 'No image or message provided'}), 400

    image = request.files['image']
    message = request.form['message'].strip()
    password = request.form.get('password', '').strip()  # Optional password

    if not image.filename or not image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return jsonify({'error': 'Please upload a PNG, JPG, or JPEG file'}), 400
    if not message:
        return jsonify({'error': 'Message cannot be empty'}), 400

    try:
        img = Image.open(image).convert("RGB")
        # Prepend password to message if provided
        secret_message = f"{password}:{message}" if password else message
        encoded_img = stepic.encode(img, secret_message.encode())

        # Generate unique filename
        filename = f"encoded_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        encoded_path = os.path.join(ENCODED_FOLDER, filename)
        encoded_img.save(encoded_path, format='PNG')

        return jsonify({'message': 'Image encoded successfully', 'encoded_image': filename})
    except Exception as e:
        return jsonify({'error': f'Encoding failed: {str(e)}'}), 500

@app.route('/decode', methods=['POST'])
def decode_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    password = request.form.get('password', '').strip()  # Optional password

    if not image.filename or not image.filename.lower().endswith('.png'):
        return jsonify({'error': 'Please upload a PNG file'}), 400

    try:
        img = Image.open(image).convert("RGB")
        decoded_message = stepic.decode(img)

        if not decoded_message:
            return jsonify({'error': 'No hidden message found or file is corrupted'}), 400

        # Check if password is present in the decoded message
        if ':' in decoded_message:
            stored_password, actual_message = decoded_message.split(':', 1)
            if stored_password != password:
                return jsonify({'error': 'Incorrect password!'}), 403
            return jsonify({'message': actual_message})
        else:
            # No password was used during encoding
            return jsonify({'message': decoded_message})
    except Exception as e:
        return jsonify({'error': f'Decoding failed: {str(e)}'}), 500

@app.route('/download_encoded/<filename>')
def download_encoded(filename):
    encoded_path = os.path.join(ENCODED_FOLDER, filename)
    if os.path.exists(encoded_path):
        return send_file(encoded_path, as_attachment=True)
    return jsonify({'error': 'Encoded image not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)