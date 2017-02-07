import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError

from app import settings
from app.models import db


@pytest.fixture(scope='session', autouse=True)
def create_database():
    """
    One thing I'm not sure about si whether this will always run
    first, and it has to run first.
    """
    engine = create_engine('postgres://postgres@/postgres')
    db_name = settings.SQLALCHEMY_DATABASE_URI.split('/')[-1]
    conn = engine.connect()
    conn.execute('commit')
    try:
        conn.execute('CREATE DATABASE %s;' % db_name)
        print('CREATE DATABASE %s;' % db_name)
    except ProgrammingError:
        print('Database %s already exists' % db_name)
        pass


@pytest.fixture(scope='session', autouse=True)
def drop_db():
    db.drop_all()
    db.create_all()


@pytest.fixture(scope='function', autouse=True)
def session():
    db.session.begin_nested()
    yield db.session
    db.session.rollback()
    db.session.remove()
