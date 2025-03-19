from fastapi import APIRouter
from starlette import status

category_router = APIRouter(
    prefix="/categories",
    tags=["Category"]
)


@category_router.get('/get', status_code=status.HTTP_200_OK)
def get_category():
    """
    Filtrlash, Kategoriyalarni olish!
    Muvaffaqiyatli: 200
    Ma'lumot topilmadi: 404
    Xatolik: 400
    :return:
    """
    pass


@category_router.post('/create', status_code=status.HTTP_201_CREATED)
def create_category():
    """
    Kategoriya qo'shish!
    Muvaffaqiyatli: 201
    Ro'yxatdan o'tmagansiz: 401
    Sizga ruxsat berilmagan: 403
    Xatolik: 400
    :return:
    """
    pass


@category_router.put('/update', status_code=status.HTTP_200_OK)
def update_categories():
    """
    Kategoriyalarni tahrirlash!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Sizga ruxsat berilmagan: 403
    Xatolik: 400
    :return:
    """
    pass


@category_router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_categories():
    """
    Kategoriyalarni o'chirish!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Sizga ruxsat berilmagan: 403
    Xatolik: 400
    :return:
    """
    pass
