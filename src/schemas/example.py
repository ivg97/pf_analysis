from typing import Optional
from datetime import datetime

from pydantic import BaseModel


# ExampleBase-схема описывает то, что мы ожидаем получить при
# создании и обновлении элементов пользовательским вводом:
# например, наименование объекта в базе данных. Время создания
# отмечается автоматически, поэтому нет необходимости указывать
# его в свойствах.
class ExampleBase(BaseModel):
    title: str


class ExampleCreate(ExampleBase):
    pass


class ExampleUpdate(ExampleBase):
    pass


# ExampleInDBBase-схема — результат выполнения методов. Это то,
# что мы будем отдавать пользователю — детальную информацию по
# нужным полям модели.
class ExampleInDBBase(ExampleBase):
    id: int
    title: str
    created_at: datetime

    class Config:
        orm_mode = True


class Example(ExampleInDBBase):
    pass


class ExampleInDB(ExampleInDBBase):
    pass
