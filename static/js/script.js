function encodeImage() {
    let imageInput = document.getElementById("imageInput");
    let messageInput = document.getElementById("messageInput");

    if (imageInput.files.length === 0 || messageInput.value.trim() === "") {
        alert("⚠️ Please upload an image and enter a message!");
        return;
    }

    let formData = new FormData();
    formData.append("image", imageInput.files[0]);
    formData.append("message", messageInput.value);

    fetch('/encode', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.encoded_image) {
            let container = document.getElementById("encodedImageContainer");
            container.innerHTML = `
                <h3 class="text-xl font-semibold glitch-text mt-4">✅ Encoded Image</h3>
                <img src="/static/encoded/${data.encoded_image}" class="mt-2 rounded-lg shadow-lg" width="300">
                <a href="/download_encoded/${data.encoded_image}" download="${data.encoded_image}" 
                   class="cyber-button mt-4">
                   ⬇️ Download Encoded Image
                </a>
            `;
        } else {
            alert("❌ Error: " + data.error);
        }
    });
}

function decodeImage() {
    let decodeImageInput = document.getElementById("decodeImageInput");

    if (decodeImageInput.files.length === 0) {
        alert("⚠️ Please upload an encoded image!");
        return;
    }

    let formData = new FormData();
    formData.append("image", decodeImageInput.files[0]);

    fetch('/decode', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            document.getElementById("decodedMessage").innerHTML = `<span class="glitch-text">🔍 Decoded Message: ${data.message}</span>`;
        } else {
            alert("❌ Error: " + data.error);
        }
    });
}
