from fastapi_chameleon import template #type: ignore
from fastapi import APIRouter

router = APIRouter()

@router.get('/courses')
async def courses():
    return{}    