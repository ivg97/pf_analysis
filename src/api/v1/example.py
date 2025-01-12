from typing import Any, List


from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db import get_session
from src.schemas import example as example_schemas
from src.services.example import example_crud

router = APIRouter()


@router.get(
    '/',
    response_model=List[example_schemas.Example]
)
async def read_examples(
        db: AsyncSession = Depends(get_session),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    # get example from db
    examples = await example_crud.get_all(
        db=db,
        skip=skip,
        limit=limit
    )
    return examples


@router.get(
    '/{example_id}',
    response_model=List[example_schemas.Example]
)
async def read_example(
        *,
        db: AsyncSession = Depends(get_session),
        example_id: int,
) -> Any:
    # get from db
    example = await example_crud.get(
        db=db,
        id=example_id
    )
    if not example:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return example


@router.post(
    '/',
    response_model=example_schemas.Example,
    status_code=status.HTTP_201_CREATED
)
async def create_example(
        example_in: example_schemas.ExampleCreate,
        db: AsyncSession = Depends(get_session),
) -> Any:
    # create item by params
    example = await example_crud.create(
        db=db,
        obj_in=example_in
    )
    return example


@router.put(
    '/{example_id}',
    response_model=example_schemas.Example,
)
async def update_example(
        *,
        example_in: example_schemas.ExampleUpdate,
        db: AsyncSession = Depends(get_session),
        example_id: int,
) -> Any:
    # get example from db
    # todo
    example = await example_crud.update(
        db=db,
        obj_in=example_in,
        id=example_id
    )
    if not example:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    # update example in db
    # todo
    return example


@router.delete('/{example_id}')
async def delete_example(
        example_id: int,
) -> Any:
    example = {}
    # get example from db
    # todo
    if not example:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    # remove item from db
    # todo
    return example
