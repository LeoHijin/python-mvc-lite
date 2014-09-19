# -*- coding: utf-8 -*-
from core.Factory import Factory
from core.DBModel import DBModel


class Collector(object):

    __Collector = None

    def __init__(self):
        self.collection = []
    #def __new__(cls):
    #    if(cls.__Collector is None):
    #        cls.__Collector = super(
    #            Collector, cls).__new__(cls)
    #        return cls.__Collector

    def __add_object(self, new_object):
        self.collection.append(new_object)

    def get(self, Object):
        class_name = Object.__class__.__name__
        class_name_low = class_name.lower()
        sql = "SELECT %s_id FROM %s WHERE %s_id > 0" % (
            class_name_low, class_name_low, class_name_low)
        results = DBModel().execute(sql)
        for row in results:
            self.__add_object(
                Factory().create_object(class_name, row[0]))
        return self.collection