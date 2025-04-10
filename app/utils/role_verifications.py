from fastapi import HTTPException


def role_verification(user, function: str):
    """
    Foydalanuvchining funksiyani bajarishga ruxsati bor-yo‘qligini tekshiradi.

    :param user: Hozirgi foydalanuvchi obyekti
    :param function: Bajarilayotgan funksiya nomi
    :raises HTTPException: Agar ruxsat bo'lmasa, 401 xato qaytaradi
    """
    allowed_functions_for_admins = {'get_users', 'create_category', 'update_categories', 'delete_categories',
                                    'delete_order',
                                    'read_order', 'create_order', 'read_orders', 'create_product', 'add_pro_image',
                                    'update_product', 'delete_products', 'get_table', 'create_table', 'update_table',
                                    'delete_table'}

    allowed_functions_for_users = {'delete_user', 'update_user', 'upload_user_file', 'get_me', 'get_product',
                                   'create_order'
                                   'get_table'}

    if user.role == 'boss':
        return True

    if user.role == 'admin' and function in allowed_functions_for_admins:
        return True

    if user.role == "user" and function in allowed_functions_for_users:
        return True

    raise HTTPException(status_code=401, detail="Sizga ushbu amalni bajarishga ruxsat berilmagan!")
