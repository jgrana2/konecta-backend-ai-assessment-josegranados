import jwt
import time
from passlib.context import CryptContext

SECRET_KEY = "mysecretkey"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
algorithm = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": time.time() + 3600})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=algorithm)
    return encoded_jwt

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)