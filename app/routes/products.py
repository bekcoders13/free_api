from fastapi import APIRouter
from starlette import status

product_router = APIRouter(
    prefix='/products',
    tags=["Product"]
)


@product_router.get('/get', status_code=status.HTTP_200_OK)
def get_product():
    """
    Mahsulotlarni olish, get qilish!
    Muvaffaqiyatli: 200
    Ma'lumot topilmadi: 404
    :return:
    """
    pass


@product_router.post('/create', status_code=status.HTTP_201_CREATED)
def create_product():
    """
    Mahsulotni bazaga qo'shish!
    Muvaffaqiyatli: 201
    Ro'yxatdan o'tmagansiz: 401
    Sizga ruxsat berilmagan: 403
    :return:
    """
    pass


@product_router.put('/rating_product', status_code=status.HTTP_200_OK)
def rating_products():
    """
    Mahsulotni reytingini baholash!
    Mahsulot muvaffaqiyatli baholandi: 200
    Mahsulot topilmadi: 404
    :return:
    """
    pass


@product_router.post('/upload_image', status_code=status.HTTP_201_CREATED)
def imaga_qoshish():
    """
    Mahsulotga rasmlar qo'shish!
    Mahsulot rasmi qo'shildi: 201
    Mahsulot topilmaid: 404
    Ro'yxatdan o'tmagansiz: 401
    Sizga ruxsat berilmagan: 403
    :return:
    """
    pass


@product_router.put('/update', status_code=status.HTTP_200_OK)
def update_product():
    """
        Mahsulot ma'lumotlarini yangilash!
        Mahsulot ma'lumotlari yangilandi: 200
        Mahsulot topilmadi: 404
        Ro'yxatdan o'tmagansiz: 401
        Sizga ruxsat berilmagan: 403
        :return:
        """
    pass


@product_router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_products():
    """
        Mahsulotni bazadan o'chirib yuborish!
        Mahsulot o'chirildi: 200
        Mahsulot topilmadi: 404
        Ro'yxatdan o'tmagansiz: 401
        Sizga ruxsat berilmagan: 403
        :return:
        """
    pass
