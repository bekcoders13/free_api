from datetime import timedelta, datetime
from typing import Optional

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm.session import Session
from starlette import status

from app.models.users import User
from app.schemas.users import CreateUser
from database import get_db
from app.schemas.token import Token, TokenData

session = Session()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 600

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")

login_router = APIRouter(
    tags=['Kirish']
)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=150)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: Optional[str] = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(phone_number=username)
    except JWTError:
        raise credentials_exception
    user = db.query(User).where(User.phone_number == token_data.phone_number).first()
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: CreateUser = Depends(get_current_user)):
    return current_user


@login_router.post("/token")
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    phone_number = form_data.username
    user = db.query(User).filter(User.phone_number == phone_number).first()
    if user:
        is_validate_password = pwd_context.verify(form_data.password, user.password)
    else:
        is_validate_password = False

    if not is_validate_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login yoki parolda xatolik",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.phone_number}, expires_delta=access_token_expires
    )
    db.query(User).filter(User.id == user.id).update({
        User.token: access_token
    })
    db.commit()
    return {'id': user.id, "role": user.role, "access_token": access_token, "token_type": "bearer"}


def token_has_expired(token: str) -> bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expiration_time = datetime.fromtimestamp(payload.get("exp"))
        current_time = datetime.utcnow()
        return current_time > expiration_time
    except JWTError:
        return False


@login_router.post("/refresh_token", response_model=Token)
async def refresh_token(
    db: Session = Depends(get_db),
    token: str = None
):
    user = db.query(User).where(User.token == token).first()
    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Token xato",
        )

    if not token_has_expired(token):
        raise HTTPException(
            status_code=400,
            detail="Token muddati tugamagan",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.phone_number},
        expires_delta=access_token_expires
    )
    db.query(User).filter(User.id == user.id).update({
        User.token: access_token
    })
    db.commit()

    return {
        'id': user.id,
        "role": user.role,
        "access_token": access_token,
        "token_type": "bearer",
    }
