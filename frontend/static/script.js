document.getElementById('uploadForm').onsubmit = async function(event) {
    event.preventDefault();
    
    let formData = new FormData();
    let fileInput = document.getElementById('fileInput');
    formData.append('file', fileInput.files[0]);
    
    let response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    
    let result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
};
