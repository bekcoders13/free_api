import datetime

from sqlalchemy import desc

from app.models.categories import Category
from app.models.products import Product
from app.utils.db_operations import get_in_db, save_in_db


def get_f(name, category_id, price, ident, limit, page, db):
    offset = (page - 1) * limit
    if ident:
        id_filter = Product.id == ident
    else:
        id_filter = Product.id > 0

    if category_id:
        c_id_filter = Product.category_id == category_id
    else:
        c_id_filter = Product.id > 0

    if price > 0:
        price_filter = Product.discount_price <= price <= Product.price
    else:
        price_filter = Product.id > 0

    if name:
        name_formatted = "%{}%".format(name)
        name_filter = Product.name.like(name_formatted)
    else:
        name_filter = Product.id > 0

    items = (db.query(Product)
             .filter(id_filter, c_id_filter, price_filter, name_filter)
             .order_by(desc(Product.id))
             .offset(offset).limit(limit).all())
    return {"data": items}


def create_f(form, db):
    get_in_db(db, Category, form.category_id)
    new_item = Product(
        category_id=form.category_id,
        name=form.name,
        price=form.price,
        amount=form.amount,
        brand=form.brand,
        description=form.description,
        discount=form.discount,
        discount_price=form.discount_price,
        discount_start=form.discount_start,
        discount_end=form.discount_end,
        created_at=datetime.date.today()
    )
    save_in_db(db, new_item)
    return {"detail": f"{form.name} mahsuloti qo'shildi!"}


def update_f(form, db):
    get_in_db(db, Product, form.ident)
    get_in_db(db, Category, form.category_id)
    db.query(Product).filter(Product.id == form.ident).update({
        Product.name: form.name,
        Product.category_id: form.category_id,
        Product.price: form.price,
        Product.amount: form.amount,
        Product.rating: form.rating,
        Product.rating_count: form.rating_count,
        Product.discount: form.discount,
        Product.discount_price: form.discount_price,
        Product.discount_start: form.discount_start,
        Product.discount_end: form.discount_end,
        Product.brand: form.brand,
        Product.description: form.description,
    })
    db.commit()
    return {"detail": f"{form.ident} iddagi ma'lumot yangilandi!"}
