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

    def _check_cache(self, name):
        cache_cutoff = datetime.datetime.now() - datetime.timedelta(minutes=5)
        if name in self.cache:
            if self.cache[name]["Creation Date"] < cache_cutoff:
                return True

    def get_list(self, path, fallback):
        if self._check_cache(path):
            ids_with_dates = self.cache[path]['List']
        else:
            ids_with_dates = fallback()
            self.cache[path]['List'] = ids_with_dates
            self.cache[path]['Creation Date'] = datetime.datetime.now()
        return ids_with_dates