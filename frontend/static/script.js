document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    let fileInput = document.getElementById('fileInput');
    if (fileInput.files.length === 0) {
        alert('Please select a file.');
        return;
    }

    let formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        let response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            let errorText = await response.text();
            throw new Error(errorText);
        }

        let result = await response.json();
        displayResult(result);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to upload image.');
    }
});

function displayResult(result) {
    let resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';

    if (result.error) {
        resultDiv.textContent = result.error;
    } else {
        result.similar_images.forEach(image => {
            let imgElement = document.createElement('img');
            imgElement.src = `/caltech-101/${image}`;
            imgElement.className = 'img-fluid img-thumbnail';
            resultDiv.appendChild(imgElement);
        });
    }
}
