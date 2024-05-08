from fastapi import FastAPI

__version__ = "1.0.0"

app = FastAPI()
@app.get("/")
async def index():
    return {
        "data": {
            "version": __version__
        }
    }