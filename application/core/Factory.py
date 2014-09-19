# -*- coding: utf-8 -*-


class Factory(object):

    def create_object(cls, class_name, id_value, id_name=''):
        exec ('from modules.%ss.controllers.%s import %s' %
        (class_name.lower(), class_name.lower(), class_name))
        obj = locals()[class_name]()
        id_name = "%s_id" % obj.__class__.__name__.lower()
        setattr(obj, id_name, id_value)
        obj.get()
        return obj