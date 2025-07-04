from datetime import datetime, timedelta, timezone
from jose import jwt 
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.entities.user import User

SECRET_KEY = "TU_SECRETO_AQUI"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60 * 24  # 1 día

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+ timedelta(minutes=EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/users/login")

