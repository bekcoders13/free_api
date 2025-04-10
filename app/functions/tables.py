from fastapi import HTTPException

from app.models.tables import Table
from app.utils.db_operations import save_in_db


def create_f(forms, db):
    for form in forms:
        new_item = Table(
            table_number=form.table_number,
            capacity=form.capacity,
            status=form.status
        )
        save_in_db(db, new_item)
    return {"detail": "muvaffaqiyatli saqlandi"}


def update_f(form, db):
    try:
        db.query(Table).filter(Table.id == form.ident).update({
            Table.table_number: form.table_number,
            Table.status: form.status,
            Table.capacity: form.capacity,
        })
        db.commit()
    except Exception as e:
        raise HTTPException(400, f"Xatolik: {e}")
    return {"detail": "muvaffaqiyatli yangilandi"}


def delete_f(ident, db):
    try:
        db.query(Table).filter(Table.id == ident).delete()
        db.commit()
    except Exception as e:
        raise HTTPException(400, f"Xatolik: {e}")
    return {"detail": "muvaffaqiyatli o'chirildi"}
