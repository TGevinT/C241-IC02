from PIL import Image
import onnxruntime as ort
from src.utils import preprocess_image_bawah, resize_image
import os
from src.gigi import Gigi
import io

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model', 'model_gigi_tampak_bawah.onnx')

class GigiTampakBawah(Gigi):
    def __init__(self, image):
        img_convert = Image.open(io.BytesIO(image)).convert('RGB')
        processed_image = preprocess_image_bawah(img_convert)
        img_resize = resize_image(img_convert)
        class_labels = ['Bengkak Gusi', 'Bukan Gambar Gigi', 'Gigi Berlubang', 'Gigi Sehat', 'Plak Gigi']
        model = ort.InferenceSession(model_path)
        bucket_name = "gigi-tampak-bawah"
        super().__init__(img_resize, processed_image, class_labels, model, bucket_name)
        