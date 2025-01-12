from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from datetime import datetime

from models.base import Base


class ExampleModel(Base):
    __tablename__ = 'example_model'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        default=datetime.now,
                        nullable=False)

