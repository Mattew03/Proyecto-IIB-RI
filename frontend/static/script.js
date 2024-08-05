function uploadImage() {
    var file = document.getElementById('imageUpload').files[0];
    var formData = new FormData();
    formData.append('file', file);

    fetch('/predict', {
        method: 'POST',
        body: formData
    }).then(response => response.json())
      .then(data => {
          var resultDiv = document.getElementById('result');
          resultDiv.innerHTML = `<p>Category: ${data.category}</p>`;
          if (data.similar_images && data.similar_images.length > 0) {
              var similarImagesHtml = '<p>Similar Images:</p><div class="similar-images">';
              data.similar_images.forEach(image => {
                  similarImagesHtml += `<img src="${image}" alt="Similar Image" class="similar-image"/>`;
              });
              similarImagesHtml += '</div>';
              resultDiv.innerHTML += similarImagesHtml;
          }
      }).catch(error => {
          console.error('Error:', error);
      });
}
