from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Base
from auth import router as auth_router
from licenses import router as license_router
from bot_api import router as bot_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="LordsBot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(license_router)
app.include_router(bot_router)


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "LordsBot API çalışıyor!"
    }


@app.get("/api/license/check")
def check_license():
    return {
        "valid": False,
        "message": "License system is not connected yet."
    }