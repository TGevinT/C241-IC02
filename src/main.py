from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.utils import preprocess_image
import tensorflow as tf

import numpy as np
import os
import sys
from tensorflow.keras.models import load_model


# # Add the parent directory of your project to the module search path
# mypath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'machine_learning/models'))
# model = tf.keras.models.load_model(os.path.join(mypath, 'model_tampak_depan.h5'))

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'machine_learning/models')))
model_path = os.path.join(os.path.dirname(__file__), '..', 'machine_learning/models', 'model_tanpak_atas.h5')
model = load_model(model_path)


__version__ = "1.0.0"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return {
        "data": {
            "version": __version__
        }
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    class_labels = ['Perubahan Warna Gigi', 'Radang Gusi', 'Gigi Berlubang', 'Gigi Sehat', 'Bukan Gigi']
    image_data = await file.read()
    processed_image = preprocess_image(image_data)
    prediction = model.predict(processed_image)
    prediction_class_index = np.argmax(prediction)

    if prediction_class_index < len(class_labels):
        predicted_label = class_labels[prediction_class_index]
        return {
            "prediksi": predicted_label,
        }
    else:
        raise HTTPException(status_code=500, detail="Predicted class index is out of range.")