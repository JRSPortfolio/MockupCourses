from fastapi_chameleon import template #type: ignore
from fastapi import APIRouter
from common import base_viewmodel_with
from services import student_services as ss

router = APIRouter()

@router.get('/account')
@template()
async def index():
    return{}    

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
    # students = ss.every_student()
    # for student in students:
    #     if student.email == email and student.password == password:
    #         return base_viewmodel_with({'user_id': student.id,
    #                                     'is_logged_in': True})
    return base_viewmodel_with({'error': False,
                                'error_msg': 'There was an error with your data. Please try again.'})

@router.get('account/{student.id}')


@router.get('/account/logout')
@template()
async def logout():
    return{} 