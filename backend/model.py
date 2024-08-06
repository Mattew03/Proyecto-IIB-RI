from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Ruta al archivo .h5 del modelo en la carpeta backend
model = load_model('backend/modelo.h5')

def predict_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # Ajusta el tamaño según tu modelo
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalización, ajusta según tu modelo
    prediction = model.predict(img_array)
    return {"prediction": prediction.tolist()}
