from flask import Flask, request, jsonify, render_template
from model import predict_image
import os

app = Flask(__name__, static_folder='../frontend/statics', template_folder='../frontend/templates')
UPLOAD_FOLDER = 'backend/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        result = predict_image(filepath)
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
