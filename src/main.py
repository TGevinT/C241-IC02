import logging
from fastapi import FastAPI, HTTPException, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.gigi_tampak_bawah import GigiTampakBawah
from src.gigi_tampak_depan import GigiTampakDepan
from src.gigi_tampak_atas import GigiTampakAtas
from datetime import datetime
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()


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

def save_images_in_background(result_depan, filename_depan, checker_tampak_depan, 
                              result_atas, filename_atas, checker_tampak_atas, 
                              result_bawah, filename_bawah, checker_tampak_bawah,
                              timestamp):
    try:
        checker_tampak_depan.save_image(result_depan, filename_depan, timestamp)
        checker_tampak_atas.save_image(result_atas, filename_atas, timestamp)
        checker_tampak_bawah.save_image(result_bawah, filename_bawah, timestamp)
        logger.info("Images saved successfully.")
    except Exception as e:
        logger.error(f"Failed to save images: {e}")

@app.post("/predict")
async def predict(
    background_tasks: BackgroundTasks,
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
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Add the task to save images in the background
    background_tasks.add_task(
        save_images_in_background,
        result_depan, tampak_depan.filename, checker_tampak_depan,
        result_atas, tampak_atas.filename, checker_tampak_atas,
        result_bawah, tampak_bawah.filename, checker_tampak_bawah,
        timestamp
    )

    return {
        "result_depan": result_depan,
        "result_atas": result_atas,
        "result_bawah": result_bawah,
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)