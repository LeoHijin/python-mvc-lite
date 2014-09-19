# -*- coding: utf-8 -*-

import MySQLdb


class DBModel (object):

    def execute(self, query):
        DB_HOST = "localhost"
        DB_USER = "root"
        DB_PASS = "root"
        BD_NAME = "suro_system"

        parameters = [DB_HOST, DB_USER, DB_PASS, BD_NAME]
        link = MySQLdb.connect(*parameters)
        pointer = link.cursor()
        pointer.execute(query)
        if(query.upper().startswith('SELECT')):
            data = pointer.fetchall()
        else:
            link.commit()
            if query.upper().startswith('INSERT'):
                data = pointer.lastrowid
            else:
                data = None
        pointer.close()
        link.close()

        return data