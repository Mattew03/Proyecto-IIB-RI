import pickle
from sklearn.neighbors import NearestNeighbors
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os


# Ruta al archivo .h5 del modelo en la carpeta backend
model = load_model('backend/modelo.h5')

# Cargar el índice k-NN
knn_index_path = 'D:\\U\\7. Septimo\\RI\\Proyecto-IIB-RI\\modelo\\knn_index.pkl'
with open(knn_index_path, 'rb') as f:
    knn_index = pickle.load(f)

def extract_features(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # Ajusta el tamaño según tu modelo
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalización, ajusta según tu modelo
    features = model.predict(img_array)
    return features.flatten()  # Aplana el vector de características

def predict_image(image_path):
    features = extract_features(image_path)
    distances, indices = knn_index.kneighbors(features.reshape(1, -1), n_neighbors=5)

    # Asumiendo que las imágenes están en el directorio 'caltech-101'
    base_dir = 'D:\\U\\7. Septimo\\RI\\ir24a\\week14\\caltech-101'
    image_files = [os.path.join(base_dir, f'{i}.jpg') for i in indices[0]]

    result = {
        'distances': distances[0].tolist(),
        'image_files': image_files
    }
    return result
