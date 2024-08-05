from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Cargar el modelo
model = load_model('modelo/modelo.h5')

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224)) # Tamaño según el modelo
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0 # Normalización si el modelo lo requiere
    
    prediction = model.predict(img_array)
    return np.argmax(prediction, axis=1) # Ajustar según el tipo de salida del modelo
