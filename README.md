# Image Steganography - Hide Secret Messages in Images

This project allows users to **encode** and **decode** secret messages within images using steganography techniques. It features an intuitive web interface for encoding messages into images and decoding hidden messages from images.

### Features:
- **Encode a message** into an image by uploading the image and typing the secret message.
- **Download** the encoded image with the hidden message.
- **Decode the message** from an image by uploading the encoded image.
- The project utilizes **HTML, CSS (Tailwind CSS), JavaScript**, and **Python (Flask)** for the back-end.

---

## Demo

You can try out the live demo at: [Insert Live Demo Link Here]

---

## Tech Stack
- **Front-end:**
  - HTML5
  - CSS (Tailwind CSS)
  - JavaScript
- **Back-end:**
  - Python (Flask)
  - Image Processing Libraries (Pillow)
  
---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/hritikranjan1/steganography-image-message.git
cd steganography-image-message
2. Set up Python environment
If you don’t have Python installed, install Python.

Create a virtual environment and activate it:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
3. Install required dependencies
Install all necessary dependencies via requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
4. Run the project locally
For local development, run the following command:

bash
Copy
Edit
python app.py
This will start the Flask server. Open your browser and visit http://127.0.0.1:5000 to view the app.

How to Use
Encoding a Message:
Upload an image using the "Choose File" button.
Enter the secret message you want to encode.
Click the "Encode & Download" button to encode the message into the image and download the encoded image.
Decoding a Message:
Upload the encoded image using the "Choose File" button under the decoding section.
Click "Decode" to reveal the hidden message inside the image.
Contributing
We welcome contributions to improve the project! Here’s how you can help:

Fork the repository.
Create a new branch.
Implement your changes.
Create a pull request to merge changes into the main repository.
Contact
Developer: Hritik Ranjan
GitHub: https://github.com/hritikranjan1
LinkedIn: https://www.linkedin.com/in/hritikranjan1/
Telegram: https://t.me/codewithluv143
