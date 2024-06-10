import numpy as np
import torchvision.transforms as transforms
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def preprocess_image_atas(image):
    transform = transforms.Compose([
        transforms.Resize((640, 640)),
        transforms.ToTensor()
    ])
    img = transform(image)  # Convert image to tensor
    img = np.array(img)    # Convert tensor to numpy array
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def preprocess_image_depan(image):
    IMAGE_SIZE = 416
    img_resized = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    img = np.array(img_resized)
    img = np.transpose(img, (2, 0, 1))  # Change dimensions from (224, 224, 3) to (3, 224, 224)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    return img

def preprocess_image_bawah(image):
    input_size=(640, 640)
    transform = transforms.Compose([
        transforms.Resize(input_size),
        transforms.ToTensor(),
    ])
    img = transform(image).unsqueeze(0).numpy()
    return img

def connect_to_database():
    conn = psycopg2.connect(
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD")
    )
    return conn