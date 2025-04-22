from datetime import date
from fastapi import HTTPException

from app.models.users import User
from app.routes.login import get_password_hash
from app.utils.db_operations import save_in_db


def get_user_f(ident, name, db):
    if ident > 0:
        ident_filter = User.id == ident
    else:
        ident_filter = User.id > 0

    if name:
        search_formatted = "%{}%".format(name)
        search_filter = (User.firstname.like(search_formatted) |
                         User.lastname.like(search_formatted))
    else:
        search_filter = User.id > 0

    items = (db.query(User)
             .filter(ident_filter, search_filter, User.role == 'user').order_by(User.id.desc()).all())
    return {"data": items}


def get_admin_f(ident, name, role, db):
    if ident > 0:
        ident_filter = User.id == ident
    else:
        ident_filter = User.id > 0

    if name:
        search_formatted = "%{}%".format(name)
        search_filter = (User.firstname.like(search_formatted) |
                         User.lastname.like(search_formatted))
    else:
        search_filter = User.id > 0

    items = (db.query(User)
             .filter(ident_filter, search_filter, User.role == role.name).order_by(User.id.desc()).all())
    return {"data": items}


def create_general_user_f(form, db):
    print(f"salom: {get_password_hash(form.password)}, password: {form.password}")
    new_item_db = User(
        firstname=form.firstname,
        lastname=form.lastname,
        phone_number=form.phone_number,
        password=get_password_hash(form.password),
        role="admin",
        created_at=date.today(),
    )
    save_in_db(db, new_item_db)
    return {"detail": "Muvaffaqiyatli!!!"}


def update_user_f(form, user, db):
    db.query(User).filter(User.id == user.id).update({
        User.firstname: form.firstname,
        User.lastname: form.lastname,
        User.password: get_password_hash(form.password),
    })
    db.commit()
    return {"detail": "Yangilandi!!!"}


def change_role_user_f(form, db):
    updated_rows = db.query(User).filter(User.id == form.id).update({
        User.role: form.role.name,
    })
    db.commit()

    if updated_rows == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"detail": "User role changed successfully"}


def delete_user_f(db, user):
    db.query(User).filter(User.id == user.id).delete()
    db.commit()
    return {"message": "User deleted!"}
