from flask_testing import TestCase
from application import app, db


class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        
        return app

    def setUp(self):
        db.create_all()
        for subj in ['Jankins', 'Pythud', 'Flop']:
            subjects = Subjects(subject_name=subj)
        db.session.add(subjects)

    def tearDown(self):
        db.drop_all()
    
class TestRead(TestBase):
    def test_dbread(self):
        var1 = db.query(Subjects).first()
        assert var1.subject_name == ''