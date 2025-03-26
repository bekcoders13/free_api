from datetime import date
from fastapi import HTTPException

from app.models.users import Users
from app.routes.login import get_password_hash, refresh_token
from app.utils.db_operations import save_in_db


def get_user_f(ident, name, db):
    if ident > 0:
        ident_filter = Users.id == ident
    else:
        ident_filter = Users.id > 0

    if name:
        search_formatted = "%{}%".format(name)
        search_filter = (Users.firstname.like(search_formatted) |
                         Users.lastname.like(search_formatted))
    else:
        search_filter = Users.id > 0

    items = (db.query(Users)
             .filter(ident_filter, search_filter, Users.role == 'user').order_by(Users.id.desc()).all())
    return {"data": items}


def get_admin_f(ident, name, role, db):
    if ident > 0:
        ident_filter = Users.id == ident
    else:
        ident_filter = Users.id > 0

    if name:
        search_formatted = "%{}%".format(name)
        search_filter = (Users.firstname.like(search_formatted) |
                         Users.lastname.like(search_formatted))
    else:
        search_filter = Users.id > 0

    items = (db.query(Users)
             .filter(ident_filter, search_filter, Users.role == role.name).order_by(Users.id.desc()).all())
    return {"data": items}


def create_general_user_f(form, db):
    new_item_db = Users(
        firstname=form.firstname,
        lastname=form.lastname,
        phone_number=form.phone_number,
        password=get_password_hash(form.password),
        role="user",
        created_at=date.today(),
    )
    save_in_db(db, new_item_db)
    return {"detail": "Muvaffaqiyatli!!!"}


def update_user_f(form, user, db):
    db.query(Users).filter(Users.id == user.id).update({
        Users.firstname: form.firstname,
        Users.lastname: form.lastname,
        Users.password: get_password_hash(form.password),
    })
    db.commit()
    return {"detail": "Yangilandi!!!"}


def change_role_user_f(form, db):
    updated_rows = db.query(Users).filter(Users.id == form.id).update({
        Users.role: form.role.name,
    })
    db.commit()

    if updated_rows == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"detail": "User role changed successfully"}


def delete_user_f(db, user):
    db.query(Users).filter(Users.id == user.id).delete()
    db.commit()
    return {"message": "User deleted!"}
