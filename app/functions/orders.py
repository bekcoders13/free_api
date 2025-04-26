from sqlalchemy.orm import Session, joinedload
from app.models.orders import Order
from app.models.order_items import OrderItem
from app.schemas.orders import OrderCreate


def create_order_f(db: Session, order_data: OrderCreate):
    order = Order(
        table_number=order_data.table_number,
        user_id=order_data.user_id,
        order_date=order_data.order_date,
        total_price=order_data.total_price,
        status=order_data.status
    )
    db.add(order)
    db.flush()  # order.id olish uchun

    for item in order_data.items:
        db_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(db_item)

    db.commit()
    db.refresh(order)

    # 👉 Bu yerda itemlar hali yuklanmagan bo'lishi mumkin!
    # Shuning uchun query orqali qayta olish:
    return db.query(Order).options(joinedload(Order.items)).filter(Order.id == order.id).first()


def get_order_f(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def get_orders_f(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Order).offset(skip).limit(limit).all()


def delete_order_f(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
        return True
    return False


def update_f(ident, status, db):
    db.query(Order).filter(Order.id == ident).update({
        Order.status: status
    })
    db.commit()
    return {"detail": "yangilandi"}
