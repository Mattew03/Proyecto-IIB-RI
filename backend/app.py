from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from model import predict_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'back/uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result = predict_image(file_path)
            return render_template('index.html', filename=filename, result=result)

if __name__ == '__main__':
    app.run(debug=True)
