from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc
from starlette import status

from app.models.tables import Table
from app.routes.login import get_current_active_user
from app.schemas.tables import CreateTable, UpdateTable
from app.functions.tables import create_f, update_f, delete_f
from app.utils.role_verifications import role_verification
from database import get_db

table_router = APIRouter(prefix='/table', tags=['Stollar'])


@table_router.get('/get', status_code=status.HTTP_200_OK)
def get_table(db: Session = Depends(get_db),
              current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'get_table')
    return {'data': db.query(Table).order_by(desc(Table.id)).all()}


@table_router.post('/create', status_code=status.HTTP_201_CREATED)
def create_table(forms: List[CreateTable], db: Session = Depends(get_db),
                 current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'create_table')
    return create_f(forms, db)


@table_router.put('/update', status_code=status.HTTP_200_OK)
def update_table(form: UpdateTable, db: Session = Depends(get_db),
                 current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'update_table')
    return update_f(form, db)


@table_router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_table(ident: int, db: Session = Depends(get_db),
                 current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'delete_table')
    return delete_f(ident, db)
