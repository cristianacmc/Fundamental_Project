from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Truffles, Categories

#create the base class 
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app
    
    def setUp(self):
        db.create_all()
        sample1 = Truffles(title="", truffle_description="", unit_price="", in_stock="", category_id="")
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        