from app.models import db
from app.models.some import SomeModel


def test_t11():
    sm = SomeModel(name='one')
    db.session.add(sm)
    db.session.commit()


def test_t12():
    # This should fail on unique constraint if rollbacks don't work
    sm = SomeModel(name='one')
    db.session.add(sm)
    db.session.commit()
