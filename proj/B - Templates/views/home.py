from fastapi_chameleon import template #type: ignore
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
@template()
async def index():
    return {'course1': 'Biologia',
            'course2': 'Contabilidade',
            'course3': 'Electronica'}



@router.get('/about')
@template()
async def about():
    return{'alguma_coisa': 'Algum texto aqui'}