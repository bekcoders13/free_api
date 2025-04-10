from app.models.categories import Category
from app.utils.db_operations import save_in_db, get_in_db


def create_f(form, db):
    new_item = Category(
        name=form.name,
        description=form.description,
    )
    save_in_db(db, new_item)
    return {"detail": f"{form.name} saqlandi!"}


def update_f(form, db):
    get_in_db(db, Category, form.ident)
    db.query(Category).filter(Category.id == form.ident).update({
        Category.name: form.name,
        Category.description: form.description,
    })
    db.commit()
    return {"detail": f"{form.ident} id dagi ma'lumot yangilandi!"}
