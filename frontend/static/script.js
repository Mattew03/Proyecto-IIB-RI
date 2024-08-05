document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("uploadForm").onsubmit = function(event) {
        event.preventDefault();
        var formData = new FormData(this);

        fetch("/upload", {
            method: "POST",
            body: formData,
        }).then(response => response.text()).then(result => {
            document.getElementById("result").innerHTML = result;
        }).catch(error => {
            console.error("Error:", error);
        });
    }
});
