from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session
from starlette import status

from app.models.categories import Category
from app.routes.login import get_current_active_user
from app.schemas.categories import CreateCategory, UpdateCategory
from app.functions.categories import create_f, update_f
from app.utils.role_verifications import role_verification
from database import get_db

category_router = APIRouter(
    prefix="/categories",
    tags=["Category"]
)


@category_router.get('/get', status_code=status.HTTP_200_OK)
def get_category(db: Session = Depends(get_db)):
    """
    Filtrlash, Kategoriyalarni olish!
    Muvaffaqiyatli: 200
    Ma'lumot topilmadi: 404
    Xatolik: 400
    :return:
    """
    return {"data": db.query(Category).order_by(desc(Category.id)).all()}


@category_router.post('/create', status_code=status.HTTP_201_CREATED)
def create_category(form: CreateCategory, db: Session = Depends(get_db),
                    current_user=Depends(get_current_active_user)):
    """
    Kategoriya qo'shish!
    Muvaffaqiyatli: 201
    Ro'yxatdan o'tmagansiz: 401
    Sizga ruxsat berilmagan: 403
    Xatolik: 400
    :return:
    """
    role_verification(current_user, 'create_category')
    return create_f(form, db)


@category_router.put('/update', status_code=status.HTTP_200_OK)
def update_categories(form: UpdateCategory, db: Session = Depends(get_db),
                      current_user=Depends(get_current_active_user)):
    """
    Kategoriyalarni tahrirlash!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Sizga ruxsat berilmagan: 403
    Xatolik: 400
    :return:
    """
    role_verification(current_user, "update_categories")
    return update_f(form, db)


@category_router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_categories(ident: int, db: Session = Depends(get_db),
                      current_user=Depends(get_current_active_user)):
    """
    Kategoriyalarni o'chirish!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Sizga ruxsat berilmagan: 403
    Xatolik: 400
    :return:
    """
    role_verification(current_user, 'delete_categories')
    try:
        db.query(Category).filter(Category.id == ident).delete()
        return {"detail": f"{ident} id dagi ma'lumot o'chirildi!"}
    except Exception as e:
        raise HTTPException(400, "Noto'g'ri id")
