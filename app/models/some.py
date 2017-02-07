from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.models import db


class SomeModel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
