#!/usr/bin/env python3
# sample regex (^|\D)\d{6}($|\D)
"""Folder and file utilities"""
from os import listdir
from os.path import isfile, join

def get_file_list(path):
    """Given a path prints a list of all files contained
    path -- Path that you want to get the file list from
    Returns list of string (file names)"""
    try:
        file_list = [f for f in listdir(path) if isfile(join(path, f))]
        print(file_list)
        return file_list
    except:
        print("Failure")
        return False
