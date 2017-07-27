#!/usr/bin/env python3
"""A simple caching system to very briefly cache the results from CSVReader and ExcelReader"""
import datetime

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Cache(metaclass=Singleton):
    def __init__(self):
        self.cache = {}

    def check_cache(self, name):
        cache_cutoff = datetime.datetime.now() - datetime.timedelta(minutes=5)
        if name in self.cache:
            if self.cache[name]["Creation Date"] < cache_cutoff:
                return True

    def get_list(self, name, list_source):
        if self.check_cache(name):
            ids_with_dates = self.cache[name]['List']
        else:
            ids_with_dates = list_source.get_list()
        return ids_with_dates