'''Внедрение зависимостей'''

from typing import Union, Annotated

from fastapi.params import Depends
from fastapi.routing import APIRouter

router = APIRouter()


async def common_parameters(
        q: Union[str, None] = None,
        skip: int = 0,
        limit: int = 100
):
    return {
        'q': q,
        'skip': skip,
        'limit': limit,
    }


@router.get('/items')
async def read_items(
        commons: Annotated[
            dict, Depends(common_parameters)
        ]
):
    # logic
    return commons


@router.get('/users')
async def read_users(commons: Annotated[
    dict, Depends(common_parameters)
]):
    return commons
