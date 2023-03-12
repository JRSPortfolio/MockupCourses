from datetime import date
from fastapi_chameleon import template #type: ignore
from fastapi import APIRouter
from common import base_viewmodel_with
from data.models import Student

router = APIRouter()

@router.get('/account')
@template()
async def index():
    return account_viewmodel()    

def account_viewmodel():
    student = Student(id = 15002,
                      name = 'Alberto Antunes',
                      email = 'alb@mail.com',
                      password = '123',
                      birth_date = date(1990, 2, 3)
                      )
    return base_viewmodel_with({'name' : student.name,
                                'email' : student.email})

@router.get('/account/register')
@template()
async def register():
    return register_viewmodel()

def register_viewmodel():
    return base_viewmodel_with({'error': False,
                                'error_msg': 'There was an error with your data. Please try again.'})

@router.get('/account/login')
@template()
async def login():
    return loggin_viewmodel()

def loggin_viewmodel():
    return base_viewmodel_with({'error': False,
                                'error_msg': 'There was an error with your data. Please try again.'})

@router.get('/account/logout')
@template()
async def logout():
    return{} 