import pickle
from sklearn.neighbors import NearestNeighbors
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
import numpy as np

# Cargar el modelo
model = load_model('backend/modelo2.h5')

# Cargar el índice k-NN
knn_index_path = 'D:\\U\\7. Septimo\\RI\\Proyecto-IIB-RI\\modelo\\knn_index2.pkl'
with open(knn_index_path, 'rb') as f:
    index_data = pickle.load(f)

# Extraer el índice k-NN y las rutas de las imágenes
knn_index = index_data
with open(r'D:\\U\\7. Septimo\\RI\\Proyecto-IIB-RI\\backend\\train_labels_cate.pkl', 'rb') as f:
        train_image_paths = pickle.load(f)

def extract_features(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalización, ajusta según tu modelo
    features = model.predict(img_array)
    return features.flatten()

def predict_image(image_path):
    features = extract_features(image_path)
    distances, indices = knn_index.kneighbors(features.reshape(1, -1))

    similar_images = [train_image_paths[i] for i in indices[0]]

    result = {
        'distances': distances[0].tolist(),
        'similar_images': similar_images
    }
    return result