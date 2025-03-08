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
    message = request.form['message']

    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img = Image.open(image)
        img = img.convert("RGB")  # Ensure image is in RGB mode

        # Encode the message using Stepic
        encoded_img = stepic.encode(img, message.encode())

        # Generate unique filename
        filename = f"encoded_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        encoded_path = os.path.join(ENCODED_FOLDER, filename)

        # Save the encoded image
        encoded_img.save(encoded_path, format='PNG')

        print(f"✅ Encoded image saved at: {encoded_path}")  # Debugging

        return jsonify({'message': 'Image encoded successfully', 'encoded_image': filename})

    except Exception as e:
        print(f"❌ Error: {e}")  # Debugging
        return jsonify({'error': str(e)}), 500

@app.route('/decode', methods=['POST'])
def decode_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img = Image.open(image)
        img = img.convert("RGB")  # Ensure it's in RGB mode

        # Decode the message using Stepic
        decoded_message = stepic.decode(img)

        return jsonify({'message': decoded_message})

    except Exception as e:
        print(f"❌ Error: {e}")  # Debugging
        return jsonify({'error': str(e)}), 500

@app.route('/download_encoded/<filename>')
def download_encoded(filename):
    encoded_path = os.path.join(ENCODED_FOLDER, filename)
    if os.path.exists(encoded_path):
        return send_file(encoded_path, as_attachment=True)
    else:
        return jsonify({'error': 'Encoded image not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
