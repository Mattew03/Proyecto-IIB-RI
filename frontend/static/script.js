document.getElementById('uploadForm').onsubmit = async (e) => {
    e.preventDefault();
    let formData = new FormData();
    formData.append('file', document.getElementById('fileInput').files[0]);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result);
};
