from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routes.login import get_current_active_user
from app.utils.role_verifications import role_verification
from database import get_db
from app.functions.orders import create_order_f, get_orders_f, get_order_f, delete_order_f
from app.schemas.orders import OrderCreate, OrderRead

order_router = APIRouter(prefix="/orders", tags=["Orders"])


@order_router.post("/", response_model=OrderRead)
def create_order(order: OrderCreate, db: Session = Depends(get_db),
                 current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'create_order')
    return create_order_f(db, order)


@order_router.get("/{order_id}", response_model=OrderRead)
def read_order(order_id: int, db: Session = Depends(get_db),
               current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'read_order')
    db_order = get_order_f(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Buyurtma topilmadi")
    return db_order


@order_router.get("/", response_model=list[OrderRead])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),
                current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'read_orders')
    return get_orders_f(db, skip=skip, limit=limit)


@order_router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db),
                 current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'delete_order')
    if delete_order_f(db, order_id):
        return {"detail": "Buyurtma o‘chirildi"}
    raise HTTPException(status_code=404, detail="Buyurtma topilmadi")
