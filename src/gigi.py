import numpy as np
import io

class Gigi:
    _class_labels = []  
    _model = None

    def __init__(self, image, processed_image):
        self._image = image
        self._processed_image = processed_image

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
