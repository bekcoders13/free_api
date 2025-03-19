from fastapi import APIRouter
from starlette import status

users_router = APIRouter(
    prefix="/users",
    tags=["Foydalanuvchi operatsiyalari"]
)


@users_router.get('/get_users', status_code=200)
def get_users():
    """
    Barcha foydalanuvchilarni olish va ularning soni!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    Muvaffaqiyatsiz: 400
    Sizga ruxsat berilmagan: 403
    :return:
    """
    pass


@users_router.get('/get_me', status_code=status.HTTP_200_OK)
def get_me():
    """
    Foydalanuvchilar o'z profillarini ko'rishi mumkin!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    Muvaffaqiyatsiz: 400
    :return:
    """
    pass


@users_router.post('/sign_up', status_code=status.HTTP_201_CREATED)
def sign_up_user():
    """
    Foydalanuvchini ro'yxatdan o'tkazish!
    Muvaffaqiyatli: 201
    Muvaffaqiyatsiz: 400
    """
    pass


@users_router.post('/upload_image', status_code=status.HTTP_201_CREATED)
def upload_user_file():
    """
    Foydalanuvchi rasmini yuklash!
    Muvaffaqiyatli: 201
    Ma'lumot topilmadi: 404
    Muvaffaqiyatsiz: 400
    """
    pass


@users_router.put("/update", status_code=status.HTTP_200_OK)
def update_user():
    """
    Foydalanuvchi ma'lumotlarini tahrirlash!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    Muvaffaqiyatsiz: 400
    """
    pass


@users_router.put('/change_role', status_code=status.HTTP_200_OK)
def update_role():
    """
    Foydalanuvchi rolini tahrirlash, admin yoki bossga ruxsat berilgan!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    Muvaffaqiyatsiz: 400
    Sizga ruxsat berilmagan: 403
    :return:
    """
    pass


@users_router.delete("/delete_own", status_code=status.HTTP_200_OK)
def delete_user():
    """
    Foydalanuvchilar o'zini o'chirib yuborishi mumkin!
    Muvaffaqiyatli: 200
    Ro'yxatdan o'tmagansiz: 401
    Ma'lumot topilmadi: 404
    Muvaffaqiyatsiz: 400
    :return:
    """
    pass
