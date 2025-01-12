from typing import List, Optional

from pydantic.fields import Field
from pydantic.main import BaseModel


class Creator(BaseModel):
    name: str
    surname: str
    birth_year: int


class CollectionItem(BaseModel):
    title: str
    pnb_year: int
    creator: Optional[Creator] = None
    tags: List[str] = []


class SomeDateTimeObject(BaseModel):
    data: str = Field(
        min_length=1,
        description='Min length must be greater than 1',
        title='Date (min 1 char)'
    )
