from datetime import date
from fastapi_chameleon import template #type: ignore
from fastapi import APIRouter, Request
from common import (base_viewmodel_with, 
                    is_valid_name,
                    form_field_as_str)
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
    return base_viewmodel_with({'name' : '',
                                'email' : '',
                                'password' : '',
                                'birth_date' : '',
                                'min_date' : '1800-01-01',
                                'max_date' : date.today(),
                                'checked' : False})

@router.post('/account/register')
@template(template_file = 'account/register.pt')
async def post_register(request: Request):
    return post_register_viewmodel(request)

async def post_register_viewmodel(request: Request):
    form_data = await request.form()
    name = form_field_as_str(form_data, 'name')
    email = form_data['email']
    
    if not is_valid_name(name):
        error, error_msg = True, 'Invalid Name!'
    else:
        error, error_msg = False, ''
    return base_viewmodel_with({'error' : error,
                                'error_msg' : error_msg,
                                'name' : name})
        
         

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