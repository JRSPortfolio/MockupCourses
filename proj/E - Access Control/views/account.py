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
from services import student_services, auth_service
from database import database_crud as db_c

router = APIRouter()

@router.get('/account')
@template()
async def index(request: Request):
    return account_viewmodel(request)    

def account_viewmodel(request: Request):
    print('get response')
    student_id = auth_service.get_auth_from_cookie(request)
    student = db_c.get_db_student_by_id(student_id)
    return ViewModel(name = student.name,       #type: ignore
                     email = student.email)     #type: ignore     

@router.post('/account')
@template(template_file = 'account/index.pt')
async def post_index(request: Request):
    vm = await post_index_viewmodel(request)
    return vm

async def post_index_viewmodel(request: Request):
    print('put request')
    form_data = await request.form()
    student_id = auth_service.get_auth_from_cookie(request)
    student = db_c.get_db_student_by_id(student_id)
    email = form_field_as_str(form_data, 'email')
    current_password = form_field_as_str(form_data, 'current_password')
    password = student_services.hash_password(current_password)
    new_password = form_field_as_str(form_data, 'new_password')
    repeat_password = form_field_as_str(form_data, 'repeat_password')
    alteration = None
    alteration_msg = None
   
    if not is_valid_email(email):
        error, error_msg = True, 'Email Inválido!'
    elif not is_valid_password(current_password):
        error, error_msg = True, 'Password Inválida!'
    elif not student_services.confirm_student_password(password, student):
        error, error_msg = True, 'Password Incorrecta!'
    elif not student_services.match_new_password(new_password, repeat_password):
        error, error_msg = True, 'Passwords Não Coincidem!'
    else:
        error, error_msg = False, ''
        
    if not error:
        if email:
            db_c.update_db_student_email(email, student)
        if new_password:
            new_password = student_services.hash_password(new_password)
            db_c.update_db_student_password(new_password, student)
        alteration, alteration_msg = True, "Dados de conta alterados."
    
    return ViewModel(error = error,
                     error_msg = error_msg,
                     name = student.name,       #type: ignore
                     email = student.email,     #type: ignore
                     alteration = alteration,
                     alteration_msg = alteration_msg)     
    
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
    if vm.error:
        return vm
    response = responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    auth_service.set_auth_cookie(response, vm.new_student_id)
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
    elif db_c.get_db_student_by_email(email):
        error, error_msg = True, f'Email {email} já Registado!'
    else:
        error, error_msg = False, ''
    
    if not error:
        student_services.create_account(name,
                                        email,
                                        password,
                                        date.fromisoformat(birth_date))
        student = db_c.get_db_student_id(email)
        new_student_id = student.id     #type: ignore
    
    return ViewModel(error = error,
                     error_msg = error_msg,
                     name = name,
                     email = email,
                     password = password,
                     birth_date = birth_date,
                     min_date = MIN_DATE,
                     max_date = date.today(),
                     checked = False,
                     new_student_id = new_student_id)
    
@router.get('/account/login')
@template()
async def login():
    return login_viewmodel()

def login_viewmodel():
    return ViewModel(email = '',
                     password = '')
    
@router.post('/account/login')
@template(template_file = 'account/login.pt')
async def post_login(request: Request):
    vm = await post_login_viewmodel(request)
    if vm.error:
        return vm
    response = responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    auth_service.set_auth_cookie(response, vm.new_student_id)
    return response

async def post_login_viewmodel(request: Request):
    form_data = await request.form()
    email = form_field_as_str(form_data, 'email')
    password = form_field_as_str(form_data, 'password')
    student_id = None

    if not is_valid_email(email):
        error, error_msg = True, 'Endereço de Email Inválido!'
    elif not is_valid_password(password):
        error, error_msg = True, 'Password Inválida!'
    elif not (student := student_services.authenticate_student_by_email(email, password)):
        error, error_msg = True, 'Dados do utilizador inválido!'
    else:
        error, error_msg = False, ''
        student = db_c.get_db_student_by_email(email)
        db_c.update_last_login(student)
        student_id = student.id     #type: ignore

    return ViewModel(error = error,
                     error_msg = error_msg,
                     email = email,
                     password = password,
                     new_student_id = student_id)

@router.get('/account/logout')
async def logout():
    response = responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    auth_service.delete_auth_cookie(response)
    return response