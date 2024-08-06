document.getElementById('uploadForm').onsubmit = async (e) => {
    e.preventDefault();
    let formData = new FormData();
    formData.append('file', document.getElementById('fileInput').files[0]);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';

    result.image_files.forEach((file, index) => {
        const img = document.createElement('img');
        img.src = `/caltech-101/${file.split('\\').pop()}`;
        img.alt = `Similar image ${index + 1}`;
        img.style.width = '200px';
        img.style.margin = '10px';
        resultDiv.appendChild(img);
    });
};