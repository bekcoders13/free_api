from fastapi import HTTPException

from app.models.employees import Employee
from app.utils.db_operations import save_in_db


def get_f(ident, position, status, db):
    if ident > 0:
        ident_filter = Employee.id == ident
    else:
        ident_filter = Employee.id > 0

    if position:
        position_formatted = "%{}%".format(position)
        position_filter = Employee.position.like(position_formatted)
    else:
        position_filter = Employee.id > 0

    if status:
        status_filter = Employee.status == status
    else:
        status_filter = Employee.id > 0

    return {"data": db.query(Employee).filter(ident_filter, position_filter, status_filter).all()}


def create_f(form, db):
    new_item = Employee(
        full_name=form.full_name,
        phone_number=form.phone_number,
        position=form.position,
        salary=form.salary,
        hire_date=form.hire_date,
        status=form.status,
    )
    save_in_db(db, new_item)
    return {"detail": "Muvaffaqiyatli saqlandi"}


def update_f(form, db):
    try:
        db.query(Employee).filter(Employee.id == form.ident).update({
            Employee.full_name: form.full_name,
            Employee.phone_number: form.phone_number,
            Employee.position: form.position,
            Employee.salary: form.salary,
            Employee.hire_date: form.hire_date,
            Employee.status: form.status,
        })
        db.commit()
    except Exception as e:
        raise HTTPException(400, f"Xatolik: {e}")
    return {"detail": "muvaffaqiyatli yangilandi"}


def delete_f(ident, db):
    try:
        db.query(Employee).filter(Employee.id == ident).delete()
        db.commit()
    except Exception as e:
        raise HTTPException(400, f"Xatolik: {e}")
    return {"detail": "muvaffaqiyatli o'chirildi"}