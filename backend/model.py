from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model = load_model('../modelo/modelo_entrenado.h5')

def predict_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # Ajusta el tamaño según tu modelo
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalización, ajusta según tu modelo
    prediction = model.predict(img_array)
    return {"prediction": prediction.tolist()}
