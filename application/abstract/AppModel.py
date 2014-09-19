# -*- coding: utf-8 -*-
from core.DBModel import DBModel
from core.Collector import Collector


class AppModel(object):

    def __init__(self):
        pass

    def exists(self):
        class_name = self._class__.__name__
        id_name = class_name.lower() + "_id"
        id_value = getattr(self, id_name)
        sql = "SELECT %s FROM %s WHERE %s = %i" % (id_name,
            class_name.lower(), id_name, id_value)
        results = DBModel().execute(sql)
        for row in results:
            obj_id = row[0]

        return not obj_id

    def compose(self, obj, cls):
        if isinstance(obj, cls) or obj is None:
            return obj
        else:
            raise TypeError('%s no es de tipo %s ' % (type(obj), cls))