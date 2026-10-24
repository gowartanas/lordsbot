from fastapi import APIRouter

import sys
import os


# ==========================================
# BOT KLASÖRÜNÜ PYTHON PATH'E EKLE
# ==========================================

BOT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "bot"
    )
)

if BOT_ROOT not in sys.path:
    sys.path.insert(0, BOT_ROOT)


# ==========================================
# GERÇEK BOT ENGINE
# ==========================================

from core.engine import BotEngine


# ==========================================
# ROUTER
# ==========================================

router = APIRouter(
    prefix="/api/bot",
    tags=["Bot"]
)


# ==========================================
# BOT ENGINE
# ==========================================

bot_engine = BotEngine()


# ==========================================
# STATUS
# ==========================================

@router.get("/status")
def get_bot_status():

    return {
        "running": bot_engine.status.value == "running",
        "status": bot_engine.status.value,
        "settings": bot_engine.settings
    }


# ==========================================
# START
# ==========================================

@router.post("/start")
def start_bot():

    success = bot_engine.start()

    return {
        "success": success,
        "running": bot_engine.status.value == "running",
        "status": bot_engine.status.value,
        "message": (
            "Bot başlatıldı."
            if success
            else "Bot zaten çalışıyor."
        )
    }


# ==========================================
# STOP
# ==========================================

@router.post("/stop")
def stop_bot():

    success = bot_engine.stop()

    return {
        "success": success,
        "running": bot_engine.status.value == "running",
        "status": bot_engine.status.value,
        "message": (
            "Bot durduruldu."
            if success
            else "Bot zaten durmuş."
        )
    }


# ==========================================
# SETTINGS
# ==========================================

@router.post("/settings")
def update_settings(settings: dict):

    bot_engine.configure(settings)

    return {
        "success": True,
        "message": "Bot ayarları güncellendi.",
        "settings": bot_engine.settings
    }