from fastapi import APIRouter
from starlette import status

orders_router = APIRouter(
    prefix="/orders",
    tags=["Order"]
)


@orders_router.get('/get', status_code=status.HTTP_200_OK)
def get_orders():
    """
    Buyurtmalarni ko'rish!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    :return:
    """
    pass


@orders_router.post('/create', status_code=status.HTTP_201_CREATED)
def create_order():
    """
    Buyurtma yaratish!
    Muvaffaqiyatli: 201
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    :return:
    """
    pass


@orders_router.put('/update', status_code=status.HTTP_200_OK)
def update_order():
    """
    Buyurtmani yangilash!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    :return:
    """
    pass


@orders_router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_order():
    """
    Buyurtmani o'chirish!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    :return:
    """
    pass
