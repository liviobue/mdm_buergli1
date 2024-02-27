// static/script.js
document.getElementById('inputForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var userInput = document.getElementById('userInput').value;
    var formData = new FormData();
    formData.append('userInput', userInput);
    var fileInput = document.getElementById('fileInput').files[0];
    if (fileInput) {
        formData.append('fileInput', fileInput);
    }

    fetch('/process_input', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(result => {
        document.getElementById('result').innerHTML = result;
    });
});
