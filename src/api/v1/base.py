import sys
from typing import Union, Optional

from fastapi import APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.responses import (
    PlainTextResponse,
    Response,
)

# from main import app
from src.schemas.base import (
    CollectionItem,
    SomeDateTimeObject,
)

from src.api.v1.example import router as example_router


router = APIRouter()
router.include_router(
    example_router,
    prefix="/example",
    tags=["example"],
)


# ---------------------------------------------------


@router.get("/")
async def root_handler():
    return {
        'version': 'v1'
    }


@router.get('/info')
async def info_handler():
    return {
        'api': 'v1',
        'python': sys.version_info,
    }


@router.get('/{action}')
async def action_handler(action):
    '''Добавляем Path-параметр'''
    return {
        'action': action
    }


@router.get('/filter')
async def filter_handler(param1, param2):
    '''Добавляем Query-параметры'''
    return {
        'action': 'filter',
        'param1': param1,
        'param2': param2
    }


@router.get('/filter')
async def filter_handler(
        param1: str,
        param2: int
) -> dict[str, Union[str, int]]:
    '''Добавляем валидацию'''
    return {
        'action': 'filter',
        'param1': param1,
        'param2': param2
    }


@router.get('/filter')
async def filter_handler(
        param1: str,
        param2: Optional[int] = None
) -> dict[str, Union[str, int]]:
    '''Добавляем необязательный параметр'''
    return {
        'action': 'filter',
        'param1': param1,
        'param2': param2
    }


@router.get(
    '/get_text',
    response_class=PlainTextResponse)
async def get_text_handler() -> str:
    '''Возвращаем обычный текст, вместо json'''
    return 'Custom text for test'


@router.get('/get_xml_data/')
def get_legacy_data():
    data = """<?xml version="1.0" encoding="UTF-8"?>
    <note>
      <to>Tove</to>
      <from>Jani</from>
      <heading>Reminder</heading>
      <body>Don't forget me this weekend!</body>
    </note>
    """
    return Response(content=data, media_type='application/xml')


@router.post(
    '/collection/',
    response_model=CollectionItem
)
async def create_item(item: CollectionItem):
    return item


# ??????????????????????????????????????????????????????


# @app.post(path='/date')
# async def get_date(request: SomeDateTimeObject):
#     return 'some response'
#
#
# @app.exception_handler(RequestValidationError)
# async def handle_error(
#         request: Request,
#         ext: RequestValidationError
# ) -> PlainTextResponse:
#     return PlainTextResponse(
#         str(ext.errors()),
#         status_code=400
#     )
