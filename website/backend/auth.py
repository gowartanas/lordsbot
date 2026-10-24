from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta
import hashlib

from database import get_db
from models import User

router = APIRouter(prefix="/api/auth")
security = HTTPBearer()

SECRET_KEY = "lordsbot-development-secret-change-before-production"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 60


class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


def hash_password(password: str):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def create_token(user_id: int, username: str):
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": str(user_id),
        "username": username,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        User.username == data.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Bu kullanıcı adı zaten kullanılıyor."
        )

    if len(data.username) < 3:
        raise HTTPException(
            status_code=400,
            detail="Kullanıcı adı en az 3 karakter olmalı."
        )

    if len(data.password) < 6:
        raise HTTPException(
            status_code=400,
            detail="Şifre en az 6 karakter olmalı."
        )

    new_user = User(
        username=data.username,
        password_hash=hash_password(data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "status": "success",
        "message": "Hesap başarıyla oluşturuldu.",
        "user_id": new_user.id,
        "username": new_user.username
    }


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        User.username == data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Kullanıcı adı veya şifre yanlış."
        )

    if user.password_hash != hash_password(data.password):
        raise HTTPException(
            status_code=401,
            detail="Kullanıcı adı veya şifre yanlış."
        )

    token = create_token(
        user.id,
        user.username
    )

    return {
        "status": "success",
        "message": "Giriş başarılı.",
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.username,
        "is_admin": user.is_admin
    }


@router.get("/me")
def get_me(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = int(payload.get("sub"))

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Geçersiz veya süresi dolmuş token."
        )

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Kullanıcı bulunamadı."
        )

    return {
        "status": "success",
        "user_id": user.id,
        "username": user.username,
        "is_admin": user.is_admin
    }
@router.get("/test")
def auth_test():
    return {
        "status": "ok",
        "message": "Auth sistemi çalışıyor!"
    }
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = int(payload.get("sub"))

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Geçersiz veya süresi dolmuş token."
        )

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Kullanıcı bulunamadı."
        )

    return user


def require_admin(
    current_user: User = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Bu işlem sadece adminler içindir."
        )

    return current_user
@router.get("/users")
def list_users(
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):
    users = db.query(User).order_by(User.id).all()

    return {
        "status": "success",
        "users": [
            {
                "id": user.id,
                "username": user.username,
                "is_admin": user.is_admin,
                "created_at": user.created_at
            }
            for user in users
        ]
    }