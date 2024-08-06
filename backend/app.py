from flask import Flask, request, jsonify, render_template, send_from_directory
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
    
@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/caltech-101/<filename>')
def send_caltech_file(filename=''):
    base_dir = 'D:\\U\\7. Septimo\\RI\\ir24a\\week14\\caltech-101'
    return send_from_directory(base_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
