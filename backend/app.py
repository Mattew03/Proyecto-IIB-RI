from flask import Flask, request, jsonify, render_template
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)
model = load_model('model.h5')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    img_file = request.files['file']
    img_path = os.path.join('uploads', img_file.filename)
    img_file.save(img_path)

    img = preprocess_image(img_path)
    prediction = model.predict(img)
    category = np.argmax(prediction, axis=1)[0]

    # Aquí iría la lógica para encontrar imágenes similares
    similar_images = find_similar_images(img)

    return jsonify({'category': int(category), 'similar_images': similar_images})

def find_similar_images(query_image):
    # Implementar lógica de búsqueda de imágenes similares
    return []

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
