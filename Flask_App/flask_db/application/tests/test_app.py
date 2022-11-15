from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Truffles

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
        # Create table
        db.create_all()

        sample1 = Truffles(title="Traditional truffle 30g", truffle_description="Slightly firm on the outside, with a soft filling and a very characteristic and delicious flavor on the inside. Here, the milk chocolate cone and the traditional truffle filling form a delicious combination.", unit_price="4.00", in_stock="40", category_id="1")
        
        # save truffle to database
        db.session.add(sample1)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
#test to check if the truffle page loads 
class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ChocolateCris Shop', response.data)
    
#test to check if Add_Truffle page loads 
class TestTruffle(TestBase):
    def test_addTruffle_get(self):
        response = self.client.get(url_for('add_truffle'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ChocolateCris Shop', response.data)

#test to check if categories page loads 
class TestCategories(TestBase):
    def test_categories_get(self):
        response = self.client.get(url_for('categories'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ChocolateCris Shop', response.data)

#test adding a truffle
class TestAddTruffle(TestBase):
    def test_add_truffle(self):
        response = self.client.post(
            url_for('add_truffle'),
            data = dict(title="Artisanal truffle grancherie 30g", truffle_description="Slightly firm on the outside, with a soft filling and a very characteristic and delicious flavor on the inside. Here, milk chocolate and cherry form a delicious combination.", unit_price=4.40, category_id=1, in_stock=25),
            follow_redirects=True
        )
        self.assertIn(b'ChocolateCris Shop',response.data)

#test updating a truffle 
class TestUpdateTruffle(TestBase):
    def test_update_truffle(self):
        response = self.client.post(
            url_for('update', title="Traditional truffle 30g", truffle_description="Slightly firm on the outside, with a soft filling and a very characteristic and delicious flavor on the inside. Here, the milk chocolate cone and the traditional truffle filling form a delicious combination.", unit_price="4.00", in_stock="40", category_id="1"),
            data = dict(title = "Traditional truffle 40g", truffle_description="Slightly firm on the outside, with a soft filling and a very characteristic and delicious flavor on the inside. Here, the milk chocolate cone and the traditional truffle filling form a delicious combination.", unit_price="4.00", in_stock="40", category_id="1"),
            follow_redirects=True
        )
        self.assertIn(b'ChocolateCris Shop', response.data)

#test deleting a trufle
class TestDel(TestBase):
    def test_delete_truffle(self):
        response = self.client.get(url_for('delete', title="Traditional truffle 30g"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ChocolateCris Shop', response.data)
