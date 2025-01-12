import os

from logging import config as logging_config
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

from src.core.logger import LOGGING

load_dotenv('.env')
logging_config.dictConfig(LOGGING)


# корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class AppSettings(BaseSettings):

    PROJECT_NAME: str = os.getenv("PROJECT_NAME", 'My project')
    PROJECT_HOST: str = os.getenv("PROJECT_HOST", '0.0.0.0')
    PROJECT_PORT: int = os.getenv("PROJECT_PORT", 8000)

    # DATABASE: реализовано для одновременного взаимодействия с alembicom
    # и базы данных
    # для alembic
    A_DB_USER: str = os.getenv('DB_USER', 'postgres')
    A_DB_PASSWORD: str = os.getenv('DB_PASSWORD', 'password')
    A_DB_HOST: str = os.getenv('DB_HOST', '0.0.0.0')
    A_DB_PORT: int = os.getenv('DB_PORT', 5432)
    A_DB_NAME: str = os.getenv('DB_NAME', 'mydb')
    A_DB_DRIVER: str = os.getenv('DB_DRIVER', 'postgresql+pg')
    # для бд
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'password'
    DB_HOST: str = '0.0.0.0'
    DB_PORT: int = 5432
    DB_NAME: str = 'mydb'
    DB_DRIVER: str = 'postgresql+pg'

    a_db_url: str = (f'{A_DB_DRIVER}://{A_DB_USER}:{A_DB_PASSWORD}'
                     f'@{A_DB_HOST}:{A_DB_PORT}/{A_DB_NAME}')

    @property
    def alembic_db_url(self):
        return self.a_db_url

    @property
    def db_url(self):
        return (f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}'
                f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}')

    class Config:
        env_file = f'{BASE_DIR[:-3]}.env'
        # env_file = f'.env'
        from_attributes = True


app_settings = AppSettings()


