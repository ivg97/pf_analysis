from models.example_model import ExampleModel
from schemas.example import ExampleCreate, ExampleUpdate
from src.services.base import RepositoryDB


class RepositoryExample(
    RepositoryDB[ExampleModel, ExampleCreate, ExampleUpdate]
):
    pass


example_crud = RepositoryExample(ExampleModel)
