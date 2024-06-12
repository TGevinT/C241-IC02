import numpy as np
import io
from google.cloud import storage
import os
from src.utils import connect_to_database
from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv("PROJECT_ID")
if not project_id:
    raise EnvironmentError("The environment variable 'PROJECT_ID' is not set.")
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id

storage_client = storage.Client()

class Gigi:

    def __init__(self, image, processed_image, class_labels, model, bucket_name):
        self._image = image
        self._processed_image = processed_image
        self._class_labels = class_labels
        self._model = model
        self._bucket_name = bucket_name

    def predict(self):
        if self._model is None:
            raise ValueError("Model is not loaded.")

        # Prepare the input
        input_name = self._model.get_inputs()[0].name
        input_data = self._processed_image.astype(np.float32)

        # Run the model
        outputs = self._model.run(None, {input_name: input_data})
        prediction = outputs[0]
        prediction_class_index = np.argmax(prediction, axis=1)[0]
        
        return self._class_labels[prediction_class_index] if prediction_class_index < len(self._class_labels) else "Unknown"
    
    def save_image(self, predict, file_name, timestamp):
        # Upload image to bucket 
        bucket = storage_client.bucket(self._bucket_name)
        blob = bucket.blob(f"{predict}/{timestamp}_{file_name}")
        blob.upload_from_string(self._image)

        image_url = blob.public_url

        conn = connect_to_database()
        cursor = conn.cursor()

        # Insert the prediction and image URL into the appropriate table
        table_name = self._bucket_name.replace("-", "_")
        insert_query = f"INSERT INTO {table_name} (image, prediction, timestamp) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (image_url, predict, timestamp))

        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()





    

