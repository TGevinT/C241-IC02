import logging
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from src.gigi_tampak_bawah import GigiTampakBawah
from src.gigi_tampak_depan import GigiTampakDepan
from src.gigi_tampak_atas import GigiTampakAtas
from datetime import datetime

import uvicorn

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
async def predict(
    tampak_depan: UploadFile = File(...),
    tampak_atas: UploadFile = File(...),
    tampak_bawah: UploadFile = File(...),
):
    
    try:
        checker_tampak_depan = GigiTampakDepan(await tampak_depan.read())
        checker_tampak_atas = GigiTampakAtas(await tampak_atas.read())
        checker_tampak_bawah = GigiTampakBawah(await tampak_bawah.read())
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}", exc_info=True)
        raise HTTPException(status_code=404, detail=f"File not found: {e}")
    except Exception as e:
        logger.error(f"Error loading models or images: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=f"Error loading models or images: {e}")
    
    try:
        result_depan = checker_tampak_depan.predict()
        result_atas = checker_tampak_atas.predict()
        result_bawah = checker_tampak_bawah.predict()
    except Exception as e:
        logger.error(f"Error during prediction: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error during prediction: {e}")
    
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        checker_tampak_depan.save_image(result_depan, tampak_depan.filename, timestamp)
        checker_tampak_atas.save_image(result_atas, tampak_atas.filename, timestamp)
        checker_tampak_bawah.save_image(result_bawah, tampak_bawah.filename, timestamp)
    except Exception as e:
        logger.error(f"Error saving images: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error saving images: {e}")

    return {
        "result_depan": result_depan,
        "result_atas": result_atas,
        "result_bawah": result_bawah,
    }
