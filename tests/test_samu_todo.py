from flask import url_for
from flask_login import current_user
from flask_testing import LiveServerTestCase
from werkzeug.security import generate_password_hash

from samu_todo_example_app import app, db
from samu_todo_example_app.models import User, Todo

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyunitreport import HTMLTestRunner
import unittest

from samuranium import Samuranium


class TestUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_dict(self):
        return dict(username=self.username, password=self.password)

    def get_user(self):
        return db.session.query(User).filter_by(username=self.username).first()


cachito = TestUser('cachito', 'cachito')


class UserTest(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        with app.app_context():
            return app

    def setUp(self):
        db.create_all()
        if not db.session.query(User).filter_by(username=cachito.username).first():
            user = User(username=cachito.username, password=generate_password_hash(cachito.password))
            db.session.add(user)
            db.session.commit()

    def get_todo_by_description(self, description):
        return Todo.query.with_parent(current_user).filter_by(description=description).first()

    def get_todo_by_id(self, id):
        return Todo.query.get(id)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        if os.path.isfile('test.db'):
            os.remove('test.db')
        self.assertFalse(os.path.isfile('test.db'))


    def test_login(self):
        self.samuranium = Samuranium(selected_browser='chrome')
        url = url_for('login')
        self.samuranium.navigate_to_url(f'{self.get_server_url()}{url}')
        title = self.samuranium.get_title()
        self.assertTrue('Login' in title)
        self.samuranium.input_text_on_element(cachito.username, 'username')
        self.samuranium.input_text_on_element(cachito.password, 'password')
        self.samuranium.click_on_element('submit')
        self.assertTrue(self.samuranium.wait_for_element('[name="todoitem"]'), 'Todo page was not loaded')


    def test_add_todo(self):
        todo_item = 'call michael jordan'
        self.test_login()
        self.samuranium.input_text_on_element(todo_item, '[name="todoitem"]')
        self.samuranium.click_on_element('Add')
        self.assertTrue(self.samuranium.wait_for_element(todo_item))