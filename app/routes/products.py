from fastapi import APIRouter, Depends, HTTPException, UploadFile, Query
from sqlalchemy.orm import Session
from starlette import status

from app.functions.files import delete_file_f, save_file_db
from app.functions.products import update_f, create_f, get_f
from app.models.products import Product
from app.routes.login import get_current_active_user
from app.schemas.products import CreateProduct, UpdateProduct
from app.utils.role_verifications import role_verification
from database import get_db

product_router = APIRouter(
    prefix='/products',
    tags=["Product"]
)


@product_router.get('/get', status_code=status.HTTP_200_OK)
def get_product(name: str = None, category_id: int = 0, price: float = 0,
                ident: int = 0, page: int = Query(1), limit: int = Query(20),
                db: Session = Depends(get_db)):
    """
    Mahsulotlarni olish, get qilish filterlash!
    Muvaffaqiyatli: 200
    Ma'lumot topilmadi: 404
    :return:
    """
    return get_f(name, category_id, price, ident, limit, page, db)


@product_router.post('/create', status_code=status.HTTP_201_CREATED)
def create_product(form: CreateProduct, db: Session = Depends(get_db),
                   current_user=Depends(get_current_active_user)):
    """
        Mahsulotni bazaga qo'shish!
        Muvaffaqiyatli: 201
        Ro'yxatdan o'tmagansiz: 401
        Sizga ruxsat berilmagan: 403
        :return:
    """
    role_verification(current_user, 'create_product')
    return create_f(form, db)


@product_router.post('/upload_image', status_code=status.HTTP_201_CREATED)
def add_pro_image(ident: int, file: UploadFile, db: Session = Depends(get_db),
                  current_user=Depends(get_current_active_user)):
    """
        Mahsulot rasmini yuklash!
        Muvaffaqiyatli: 201
        Ma'lumot topilmadi: 404
        Muvaffaqiyatsiz: 400
        :return:
    """
    role_verification(current_user, 'add_pro_image')
    file_info = db.query(Product).filter(Product.id == ident).first()
    if file_info.image_path:
        delete_file_f(Product, ident, db=db)
    item = save_file_db(Product, ident, file, db)
    return item


@product_router.put('/update', status_code=status.HTTP_200_OK)
def update_product(form: UpdateProduct, db: Session = Depends(get_db),
                   current_user=Depends(get_current_active_user)):
    """
        Mahsulot ma'lumotlarini yangilash!
        Mahsulot ma'lumotlari yangilandi: 200
        Mahsulot topilmadi: 404
        Ro'yxatdan o'tmagansiz: 401
        Sizga ruxsat berilmagan: 403
        :return:
    """
    role_verification(current_user, 'update_product')
    return update_f(form, db)


@product_router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_products(ident: int, db: Session = Depends(get_db),
                    current_user=Depends(get_current_active_user)):
    """
        Mahsulotni bazadan o'chirib yuborish!
        Mahsulot o'chirildi: 200
        Mahsulot topilmadi: 404
        Ro'yxatdan o'tmagansiz: 401
        Sizga ruxsat berilmagan: 403
        :return:
    """
    role_verification(current_user, 'delete_products')
    try:
        db.query(Product).filter(Product.id == ident).delete()
        db.commit()
        return {"detail": f"{ident} id o'chirildi!"}
    except Exception as e:
        raise HTTPException(400, f'Xatolik: {e}')
