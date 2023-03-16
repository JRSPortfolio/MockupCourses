from datetime import date
from fastapi_chameleon import template #type: ignore
from fastapi import APIRouter, Request, responses, status
from infrastructure.common import (is_valid_name,
                    form_field_as_str,
                    is_valid_birth_date,
                    is_valid_password,
                    is_valid_email,
                    MIN_DATE)
from infrastructure.viewmodel import ViewModel
from data.models import Student
from services import student_services

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
    return ViewModel(name = student.name,
                     email = student.email)

@router.get('/account/register')
@template()
async def register():
    return register_viewmodel()

def register_viewmodel():
    return ViewModel(name = '',
                     email = '',
                     password = '',
                     birth_date = '',
                     min_date = MIN_DATE,
                     max_date = date.today(),
                     checked = False)

@router.post('/account/register')
@template(template_file = 'account/register.pt')
async def post_register(request: Request):
    vm = await post_register_viewmodel(request)
    # if vm.error: erro ver depois
    if vm['error']:
        return vm
    response = responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    return response

async def post_register_viewmodel(request: Request):
    form_data = await request.form()
    name = form_field_as_str(form_data, 'name')
    email = form_field_as_str(form_data, 'email')
    password = form_field_as_str(form_data, 'password')
    birth_date = form_field_as_str(form_data, 'birth_date')
    new_student_id = None
    
    if not is_valid_name(name):
        error, error_msg = True, 'Nome Inválido!'
    elif not is_valid_email(email):
        error, error_msg = True, 'Email Inválido!'
    elif not is_valid_password(password):
        error, error_msg = True, 'Password Inválida!'
    elif not is_valid_birth_date(birth_date):
        error, error_msg = True, 'Data de Nascimento Inválida!'
    elif student_services.get_student_by_email(email):
        error, error_msg = True, f'Email {email} já Registado!'
    else:
        error, error_msg = False, ''
    
    if not error:
        new_student_id = student_services.create_account(name,
                                        email,
                                        password,
                                        date.fromisoformat(birth_date)).id
    
    return ViewModel(error = error,
                     error_msg = error_msg,
                     name = name,
                     email = email,
                     password = password,
                     birth_date = birth_date,
                     min_date = MIN_DATE,
                     max_date = date.today(),
                     checked = False,
                     user_id= new_student_id)
    
@router.get('/account/login')
@template()
async def login():
    return login_viewmodel()

def login_viewmodel():
    return ViewModel(error = False,
                     error_msg = 'There was an error with your data. Please try again.')

@router.get('/account/logout')
@template()
async def logout():
    return{} 