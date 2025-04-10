from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from app.schemas.employees import CreateEmployee, UpdateEmployee, StatusType
from app.functions.employees import get_f, create_f, delete_f, update_f
from app.routes.login import get_current_active_user
from app.utils.role_verifications import role_verification
from database import get_db

employee_router = APIRouter(prefix='/employee', tags=['Xodimlar'])


@employee_router.get('/get', status_code=status.HTTP_200_OK)
def get_employee(ident: int = 0, position: str = None, statusType: StatusType = None,
                 db: Session = Depends(get_db),
                 current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'get_employee')
    return get_f(ident, position, statusType, db)


@employee_router.post('/create', status_code=status.HTTP_201_CREATED)
def create_employee(form: CreateEmployee, db: Session = Depends(get_db),
                    current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'create_employee')
    return create_f(form, db)


@employee_router.put('/update', status_code=status.HTTP_200_OK)
def update_employee(form: UpdateEmployee, db: Session = Depends(get_db),
                    current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'update_employee')
    return update_f(form, db)


@employee_router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_employee(ident: int, db: Session = Depends(get_db),
                    current_user=Depends(get_current_active_user)):
    role_verification(current_user, 'delete_employee')
    return delete_f(ident, db)
