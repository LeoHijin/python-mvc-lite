# -*- coding: utf-8 *-*


import os
import sys

sys.path.append('/var/www/pylite.local/application')


def application(environ, start_response):
    peticiones = environ['REQUEST_URI'].split('/')
    peticiones.pop(0)
    cantidad = len(peticiones)
    if cantidad == 3:
        modulo, modelo, recurso = peticiones
        arg = ''
    elif cantidad == 4:
        modulo, modelo, recurso, arg = peticiones
    else:
        modulo = 'users'
        modelo = 'user'
        recurso = 'index'
        arg = ''

    controller_name = '%sController' % modelo.capitalize()
    from sys import path
    path.append(environ['SCRIPT_FILENAME'].replace('frontcontroller.py', ''))
    exec ('from modules.%s.controllers.%s import %s' %
        (modulo, modelo, controller_name))
    controller = locals()[controller_name](recurso, arg, environ)
    output = controller.output
    start_response('200 OK', [('Content-Type',
        'text/html; charset=UTF-8')])
    return output