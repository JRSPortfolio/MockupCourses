from fastapi_chameleon import template #type: ignore
from fastapi import APIRouter
from common import base_viewmodel_with

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
    return base_viewmodel_with({'error': False,
                                'error_msg': 'There was an error with your data. Please try again.'})

@router.get('/account/logout')
@template()
async def logout():
    return{} 