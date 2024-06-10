from PIL import Image
import onnxruntime as ort
from src.utils import preprocess_image_depan
import os
from src.gigi import Gigi
import io

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model', 'model_gigi_tampak_depan.onnx')

class GigiTampakDepan(Gigi):
    def __init__(self, image):
        img_convert = Image.open(io.BytesIO(image)).convert('RGB')
        processed_image = preprocess_image_depan(img_convert)
        class_labels = ['Bukan Gambar Gigi', 'Gigi Berlubang', 'Gigi Sehat', 'Perubahan Warna Gigi', 'Radang Gusi']
        model = ort.InferenceSession(model_path)
        bucket_name = "gigi-tampak-depan"
        super().__init__(image, processed_image, class_labels, model, bucket_name)