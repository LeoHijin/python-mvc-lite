# -*- coding: utf-8 -*-

from modules.users.models import User
from modules.users.views import UserView
from core.Collector import Collector
import urllib


class UserController(object):

    def __init__(self, recurso='', arg='', environ={}):
        self.pd = environ['wsgi.input'].read() \
        if 'wsgi.input' in environ else ''
        getattr(self, recurso)((arg))

    def index(self, *arg):
        users = Collector().get(User())
        view = UserView()
        self.output = view.index(users)

    def add(self, *arg):
        view = UserView()
        self.output = view.form_add()

    def edit(self, arg):
        ide = int(arg)
        model = User()
        model.user_id = ide
        model.get()
        view = UserView()
        self.output = view.form_edit(model)

    def view(self, arg):
        ide = int(arg)
        model = User()
        model.user_id = ide
        model.get()
        view = UserView()
        self.output = view.view(model)

    def save(self, *arg):
        post = self.pd.split('&')
        _POST = {}
        for par in post:
            field, value = par.split('=')
            _POST[field] = value
        model = User()
        model.user_id = int(_POST['user_id'] if 'user_id' in _POST else 0)
        model.name = _POST['name']
        model.email = _POST['email']
        model.save()
        self.index()

    def delete(self, ide):
        ide = int(ide)
        model = User()
        model.user_id = ide
        model.destroy()
        self.index()