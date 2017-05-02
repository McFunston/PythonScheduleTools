#!/usr/bin/env python3
# sample regex (^|\D)\d{6}($|\D)
"""Given a path prints a list of all files contained"""
from os import listdir
from os.path import isfile, join

def get_file_list(path):
    try:
        file_list = [f for f in listdir(path) if isfile(join(path, f))]
        print(file_list)
        return True
    except:
        print("Failure")
        return False

get_file_list("/Users/MicaFunston/Documents")