from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import secrets

from pydantic import BaseModel

from database import get_db
from models import License, User
from auth import require_admin


router = APIRouter(prefix="/api/licenses")

security = HTTPBearer()

SECRET_KEY = "lordsbot-development-secret-change-before-production"
ALGORITHM = "HS256"


# ============================================================
# LİSANS ANAHTARI OLUŞTUR
# ============================================================

def generate_license_key():

    parts = []

    for _ in range(4):
        parts.append(
            secrets.token_hex(2).upper()
        )

    return "-".join(parts)


# ============================================================
# LİSANS OLUŞTUR
# ============================================================

@router.post("/create")
def create_license(
    days: int = 30,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):

    if days <= 0:
        raise HTTPException(
            status_code=400,
            detail="Geçerlilik süresi 0'dan büyük olmalı."
        )

    key = generate_license_key()

    while db.query(License).filter(
        License.key == key
    ).first():

        key = generate_license_key()

    license_item = License(
        key=key,
        active=True,
        expires_at=datetime.utcnow() + timedelta(
            days=days
        )
    )

    db.add(license_item)
    db.commit()
    db.refresh(license_item)

    return {
        "status": "success",
        "message": "Lisans oluşturuldu.",
        "license_id": license_item.id,
        "key": license_item.key,
        "days": days,
        "expires_at": license_item.expires_at
    }


# ============================================================
# LİSANS KONTROL
# ============================================================

@router.get("/check/{license_key}")
def check_license(
    license_key: str,
    db: Session = Depends(get_db)
):

    license_item = db.query(License).filter(
        License.key == license_key
    ).first()

    if not license_item:
        raise HTTPException(
            status_code=404,
            detail="Lisans bulunamadı."
        )

    if not license_item.active:
        return {
            "valid": False,
            "message": "Lisans pasif."
        }

    if (
        license_item.expires_at
        and license_item.expires_at < datetime.utcnow()
    ):
        return {
            "valid": False,
            "message": "Lisansın süresi dolmuş."
        }

    return {
        "valid": True,
        "message": "Lisans geçerli.",
        "license_id": license_item.id,
        "expires_at": license_item.expires_at,
        "device_bound": (
            license_item.device_id is not None
        )
    }


# ============================================================
# LİSANSI KULLANICIYA BAĞLA
# ============================================================

class AssignLicenseRequest(BaseModel):

    license_key: str
    user_id: int


@router.post("/assign")
def assign_license(
    data: AssignLicenseRequest,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):

    license_item = db.query(License).filter(
        License.key == data.license_key
    ).first()

    if not license_item:
        raise HTTPException(
            status_code=404,
            detail="Lisans bulunamadı."
        )

    user = db.query(User).filter(
        User.id == data.user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Kullanıcı bulunamadı."
        )

    license_item.user_id = user.id

    db.commit()
    db.refresh(license_item)

    return {
        "status": "success",
        "message": "Lisans kullanıcıya bağlandı.",
        "license_id": license_item.id,
        "license_key": license_item.key,
        "user_id": user.id,
        "username": user.username
    }


# ============================================================
# TOKEN İLE KULLANICI BUL
# ============================================================

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    db: Session = Depends(get_db)
):

    try:

        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = int(
            payload.get("sub")
        )

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Geçersiz veya süresi dolmuş token."
        )

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="Kullanıcı bulunamadı."
        )

    return user


# ============================================================
# KULLANICININ LİSANSINI GÖR
# ============================================================

@router.get("/my")
def my_license(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    license_item = db.query(License).filter(
        License.user_id == current_user.id,
        License.active == True
    ).order_by(
        License.expires_at.desc()
    ).first()

    if not license_item:
        return []

    return [
        {
            "id": license_item.id,
            "key": license_item.key,
            "active": license_item.active,
            "expires_at": license_item.expires_at,
            "device_bound": (
                license_item.device_id is not None
            )
        }
    ]


# ============================================================
# CİHAZ KONTROL
# ============================================================

class DeviceCheckRequest(BaseModel):

    license_key: str
    device_id: str


@router.post("/device-check")
def device_check(
    data: DeviceCheckRequest,
    db: Session = Depends(get_db)
):

    device_id = data.device_id.strip()

    if not device_id:

        raise HTTPException(
            status_code=400,
            detail="Cihaz kimliği boş olamaz."
        )

    license_item = db.query(License).filter(
        License.key == data.license_key
    ).first()

    if not license_item:

        raise HTTPException(
            status_code=404,
            detail="Lisans bulunamadı."
        )

    if not license_item.active:

        return {
            "valid": False,
            "message": "Lisans pasif."
        }

    if (
        license_item.expires_at
        and license_item.expires_at < datetime.utcnow()
    ):

        return {
            "valid": False,
            "message": "Lisansın süresi dolmuş."
        }

    if license_item.user_id is None:

        return {
            "valid": False,
            "message": (
                "Lisans henüz bir kullanıcıya bağlanmamış."
            )
        }

    if not license_item.device_id:

        license_item.device_id = device_id

        db.commit()
        db.refresh(license_item)

        return {
            "valid": True,
            "message": "Lisans bu cihaza bağlandı.",
            "device_bound": True,
            "first_activation": True
        }

    if license_item.device_id == device_id:

        return {
            "valid": True,
            "message": "Cihaz doğrulandı.",
            "device_bound": True,
            "first_activation": False
        }

    return {
        "valid": False,
        "message": "Bu lisans başka bir cihaza bağlı.",
        "device_bound": True
    }


# ============================================================
# TÜM LİSANSLARI LİSTELE
# ============================================================

@router.get("/list")
def list_licenses(
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):

    licenses = db.query(License).order_by(
        License.id.desc()
    ).all()

    result = []

    for license_item in licenses:

        username = None

        if license_item.user_id:

            user = db.query(User).filter(
                User.id == license_item.user_id
            ).first()

            if user:
                username = user.username

        result.append(
            {
                "id": license_item.id,
                "key": license_item.key,
                "user_id": license_item.user_id,
                "username": username,
                "active": license_item.active,
                "expires_at": license_item.expires_at,
                "device_bound": (
                    license_item.device_id is not None
                )
            }
        )

    return {
        "status": "success",
        "licenses": result
    }


# ============================================================
# LİSANSI AKTİF / PASİF YAP
# ============================================================

@router.post("/toggle/{license_id}")
def toggle_license(
    license_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):

    license_item = db.query(License).filter(
        License.id == license_id
    ).first()

    if not license_item:

        raise HTTPException(
            status_code=404,
            detail="Lisans bulunamadı."
        )

    license_item.active = not license_item.active

    db.commit()
    db.refresh(license_item)

    return {
        "status": "success",
        "license_id": license_item.id,
        "active": license_item.active
    }


# ============================================================
# CİHAZ BAĞLANTISINI SIFIRLA
# ============================================================

@router.post("/reset-device/{license_id}")
def reset_device(
    license_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):

    license_item = db.query(License).filter(
        License.id == license_id
    ).first()

    if not license_item:

        raise HTTPException(
            status_code=404,
            detail="Lisans bulunamadı."
        )

    license_item.device_id = None

    db.commit()
    db.refresh(license_item)

    return {
        "status": "success",
        "message": "Cihaz bağlantısı sıfırlandı.",
        "license_id": license_item.id
    }