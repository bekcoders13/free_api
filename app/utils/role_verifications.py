from fastapi import HTTPException


def role_verification(user, function: str):
    """
    Foydalanuvchining funksiyani bajarishga ruxsati bor-yo‘qligini tekshiradi.

    :param user: Hozirgi foydalanuvchi obyekti
    :param function: Bajarilayotgan funksiya nomi
    :raises HTTPException: Agar ruxsat bo'lmasa, 401 xato qaytaradi
    """
    allowed_functions_for_admins = {'get_users'}
    allowed_functions_for_users = {}

    if user.role == 'boss':
        return True

    if user.role == 'admin' and function in allowed_functions_for_admins:
        return True

    if user.role == "user" and function in allowed_functions_for_users:
        return True

    raise HTTPException(status_code=401, detail="Sizga ushbu amalni bajarishga ruxsat berilmagan!")
