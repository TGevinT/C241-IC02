from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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