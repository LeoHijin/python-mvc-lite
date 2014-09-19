# -*- coding: utf-8 -*-
from abstract.AppView import AppView


class UserView(AppView):

    def __init__(self):
        pass

    def index(self, users):
        view = self.get_view('users/index.html')
        match = self.get_match("USERS", view)
        render = ""
        for user in users:
            datas = dict(
                user_id=user.user_id,
                name=user.name,
                email=user.email
            )
            render += self.susbtitute(match, datas)
        render = view.replace(match, render)
        return self.render_gui('template.html', render)

    def form_add(self):
        view = self.get_view('users/add.html')
        return self.render_gui('template.html', view)

    def form_edit(self, user):
        view = self.get_view("users/edit.html")
        user_data = dict(
            user_id=user.user_id,
            name=user.name,
            email=user.email
        )
        render = self.susbtitute(view, user_data)
        return self.render_gui('template.html', render)

    def view(self, user):
        view = self.get_view("users/view.html")
        user_data = dict(
            user_id=user.user_id,
            name=user.name,
            email=user.email
        )
        render = self.susbtitute(view, user_data)
        return self.render_gui('template.html', render)