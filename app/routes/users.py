from fastapi import APIRouter, Depends, Body, UploadFile
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status

from app.functions.files import delete_file_f, save_file_db
from app.functions.users import (get_user_f, get_admin_f, create_general_user_f, update_user_f,
                                 change_role_user_f, delete_user_f)
from app.models.users import User
from app.routes.login import get_current_active_user
from app.schemas.users import GetUser, GetAdmin, CreateUser, UpdateUser, UpdateRole
from app.utils.role_verifications import role_verification
from database import get_db

users_router = APIRouter(
    prefix="/users",
    tags=["Foydalanuvchi operatsiyalari"]
)


@users_router.get('/get_users',
                  summary="Foydalanuvchilarni olish",
                  status_code=status.HTTP_200_OK)
def get_users(form: GetUser = Depends(GetUser), db: Session = Depends(get_db),
              current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'get_users')
    """
    Barcha foydalanuvchilarni olish va ularning soni!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    Muvaffaqiyatsiz: 400
    Sizga ruxsat berilmagan: 403
    :return:
    """
    role_verification(current_user, 'get_users')
    return get_user_f(form.id, form.name, db)


@users_router.get('/get_admins', status_code=status.HTTP_200_OK)
def get_admins(form: GetAdmin = Depends(GetAdmin), db: Session = Depends(get_db),
               current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'get_admins')
    """
        Bu boss role uchun ruxsat berilgan, berilgan role bo'yicha foydalanuvchilarni olish
        Muvaffaqiyatli: 200
        Ro'yxatdan o'tmagansiz: 401
        Ma'lumot topilmadi: 404
        Muvaffaqiyatsiz: 400
        Sizga ruxsat berilmagan: 403
        :return:
    """
    role_verification(current_user, 'get_admins')
    return get_admin_f(form.id, form.name, form.role, db)


@users_router.get('/get_me', status_code=status.HTTP_200_OK)
def get_me(db: Session = Depends(get_db),
           current_user=Depends(get_current_active_user)):
    """
    Foydalanuvchilar o'z profillarini ko'rishi mumkin!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    Muvaffaqiyatsiz: 400
    :return:
    """
    return {'data': (db.query(User)
                     .filter(User.id == current_user.id).all())}


@users_router.post('/sign_up', status_code=status.HTTP_201_CREATED)
def sign_up_user(form: Annotated[CreateUser, Body(examples=[
    {
        "firstname": "Sherzodbek",
        "lastname": "Madaminov",
        "phone_number": "+998912345678",
        "password": '********',
    }
])], db: Session = Depends(get_db)):
    """
    Foydalanuvchini ro'yxatdan o'tkazish!
    Muvaffaqiyatli: 201
    Muvaffaqiyatsiz: 400
    :return:
    """
    return create_general_user_f(form, db)


@users_router.post('/upload_image', status_code=status.HTTP_201_CREATED)
def upload_user_file(file: UploadFile,
                     db: Session = Depends(get_db),
                     current_user=Depends(get_current_active_user)):
    """
        Foydalanuvchi rasmini yuklash!
        Muvaffaqiyatli: 201
        Ma'lumot topilmadi: 404
        Muvaffaqiyatsiz: 400
        :return:
    """
    file_info = db.query(User).filter(User.id == current_user.id).first()
    if file_info.image_path:
        delete_file_f(User, current_user.id, db=db)
    item = save_file_db(User, current_user.id, file, db)
    return item


@users_router.put("/update", status_code=status.HTTP_200_OK)
def update_user(form: Annotated[UpdateUser, Body(examples=[
    {
        "firstname": "Asilbek",
        "lastname": "Tojaliyev",
        "password": '********',
    }
])], db: Session = Depends(get_db),
                current_user=Depends(get_current_active_user)):
    """
    Foydalanuvchi ma'lumotlarini tahrirlash!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    Muvaffaqiyatsiz: 400
    :return:
    """
    return update_user_f(form, current_user, db)


@users_router.put('/change_role', status_code=status.HTTP_200_OK)
def update_role(form: UpdateRole = Depends(UpdateRole), db: Session = Depends(get_db),
                current_user=Depends(get_current_active_user)):
    role_verification(current_user, "update_role")
    """
        Foydalanuvchi rolini tahrirlash, admin yoki bossga ruxsat berilgan!
        Muvaffaqiyatli: 200
        Ro'yxatdan o'tmagansiz: 401
        Ma'lumot topilmadi: 404
        Muvaffaqiyatsiz: 400
        Sizga ruxsat berilmagan: 403
        :return:
    """
    role_verification(current_user, 'update_role')
    return change_role_user_f(form=form, db=db)


@users_router.delete("/delete_own", status_code=status.HTTP_200_OK)
def delete_user(db: Session = Depends(get_db),
                current_user=Depends(get_current_active_user)):
    """
    Foydalanuvchilar o'zini o'chirib yuborishi mumkin!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    Muvaffaqiyatsiz: 400
    :return:
    """
    return delete_user_f(db, current_user)
