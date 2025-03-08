
# Image Steganography - Hide Secret Messages in Images

This project allows users to **encode** and **decode** secret messages within images using **steganography** techniques. It features an intuitive web interface for encoding messages into images and decoding hidden messages from images.

## Features
- **Encode a Message**: Upload an image and type the secret message to encode.
- **Download Encoded Image**: Once the message is encoded, download the image with the hidden message.
- **Decode the Message**: Upload an encoded image to extract and reveal the hidden message.

The project utilizes the following technologies:
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Backend**: Python (Flask), Image Processing Libraries (Pillow)

---

## Demo

You can try out the live demo of this project at:  
**[Insert Live Demo Link Here]**

---

## Tech Stack

- **Frontend**:
  - HTML5
  - CSS (Tailwind CSS)
  - JavaScript
- **Backend**:
  - Python (Flask)
  - Image Processing Libraries (Pillow)

---

## Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/hritikranjan1/image_steganography_app
cd image_steganography_app
```

### 2. Set up Python Environment

If you don’t have Python installed, install it from [python.org](https://www.python.org/downloads/).

Create a virtual environment to isolate the dependencies:

- For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

- For Windows:

```bash
python3 -m venv venv
venv\Scriptsctivate
```

### 3. Install Required Dependencies

Once the virtual environment is activated, install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Project Locally

To start the Flask server for local development, run the following command:

```bash
python app.py
```

This will start the Flask server. Open your browser and visit:

**[http://127.0.0.1:5000](http://127.0.0.1:5000)** to view the app.

---

## How to Use

### Encoding a Message:

1. **Upload an Image**: Click on the **"Choose File"** button to upload an image.
2. **Enter the Secret Message**: Type the message you want to encode into the image in the provided input field.
3. **Encode & Download**: After entering the secret message, click the **"Encode & Download"** button. The system will encode the message within the image and allow you to download the modified image with the hidden message.

### Decoding a Message:

1. **Upload the Encoded Image**: Click on the **"Choose File"** button under the decoding section to upload the image containing the hidden message.
2. **Decode the Message**: Click the **"Decode"** button to extract and reveal the hidden message from the image.

---

## Contributing

We welcome contributions to improve the project! Here's how you can help:

1. **Fork the Repository**: Click the "Fork" button at the top of the repository page to create a copy of the repository on your GitHub account.
2. **Create a New Branch**: Create a new branch for your changes:
    ```bash
    git checkout -b feature-name
    ```
3. **Make Your Changes**: Implement your improvements or fixes in the code.
4. **Commit Your Changes**: Once you're satisfied with your changes, commit them with a descriptive message:
    ```bash
    git commit -am "Added new feature"
    ```
5. **Push to the Repository**: Push your changes to the forked repository:
    ```bash
    git push origin feature-name
    ```
6. **Create a Pull Request**: Open a pull request to merge your changes into the main repository.

---

## Contact

Developer: Hritik Ranjan  
GitHub: [https://github.com/hritikranjan1](https://github.com/hritikranjan1)  
LinkedIn: [https://www.linkedin.com/in/hritikranjan1/](https://www.linkedin.com/in/hritikranjan1/)  
Telegram: [https://t.me/codewithluv143](https://t.me/codewithluv143)

---

## License

This project is open source and available under the [MIT License](LICENSE).
