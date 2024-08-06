from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
from model import predict_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'backend/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        prediction = predict_image(filepath)
        os.remove(filepath)
        return jsonify(prediction)
    return "Error during file upload", 500

if __name__ == '__main__':
    app.run(debug=True)
