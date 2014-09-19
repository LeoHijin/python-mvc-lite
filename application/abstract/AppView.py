# -*- coding: utf-8 -*-
from string import Template
import re
from settings import WEB_ROOT


class AppView(object):

    def __init__(self):
        pass

    def get_view(self, view_name):
        with open(WEB_ROOT + view_name, "r") as archivo:
            view = archivo.read()
        return view

    def get_match(self, marker, view):
        regex = re.compile("<!--%s-->(.|\n){1,}<!--%s-->" % (marker, marker))
        match = regex.search(view).group(0)
        return match

    def susbtitute(self, objective, data):
        result = Template(objective).safe_substitute(data)
        return result

    def render_gui(self, template_name, view):
        template = self.get_view(template_name)
        template_dicc = dict(
            title='TEST MVC PYTHON',
            content=view,
        )
        GUI = self.susbtitute(template, template_dicc)
        return GUI