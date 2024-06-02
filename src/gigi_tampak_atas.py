from PIL import Image
import onnxruntime as ort
from src.utils import preprocess_image_atas
import os
from src.gigi import Gigi
import io

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model', 'model_gigi_tampak_atas.onnx')



class GigiTampakAtas(Gigi):
    def __init__(self, image):
        img_convert = Image.open(io.BytesIO(image)).convert('RGB')
        processed_image = preprocess_image_atas(img_convert)
        super().__init__(img_convert, processed_image)
        self._class_labels = ['Bengkak Gusi', 'Bukan Gambar Gigi', 'Gigi Berlubang', 'Gigi Sehat', 'Plak Gigi']
        self._model = ort.InferenceSession(model_path)
