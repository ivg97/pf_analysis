from typing import (
    Any,
    Dict,
    Generic,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db import db
from models.base import Base


class Repository:
    """
    Класс Repository — это контракт или договоренность,
    какие методы будут созданы, для реализации CRUD
    """
    def get(self, *args, **kwargs):
        raise NotImplementedError

    def get_all(self, *args, **kwargs):
        raise NotImplementedError

    def create(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError


ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class RepositoryDB(
    Repository,
    Generic[ModelType, CreateSchemaType, UpdateSchemaType],
):
    def __init__(self, model: Type[ModelType]):
        self._model = model

    async def get(
            self,
            db: AsyncSession,
            id: Any,
    ) -> Optional[ModelType]:
        statement = select(
            self._model
        ).where(
            self._model.id == id
        )
        results = await db.execute(statement=statement)
        return results.scalar_one_or_none()

    async def get_all(
            self,
            db: AsyncSession,
            *,
            skip=0,
            limit=100
    ) -> List[ModelType]:
        statement = select(
            self._model
        ).offset(skip).limit(limit)
        results = await db.execute(statement=statement)
        return results.scalars().all()

    async def create(
            self,
            db: AsyncSession,
            *,
            obj_in: CreateSchemaType,
    ) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_odj = self._model(**obj_in_data)
        db.add(db_odj)
        await db.commit()
        await db.refresh(db_odj)
        return db_odj

    async def update(
            self,
            db: AsyncSession,
            *,
            db_odj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        # todo
        return db_odj

    async def delete(
            self,
            db: AsyncSession,
            *,
            id: int
    ) -> ModelType:
        # todo
        db_obj = ModelType
        return db_obj
