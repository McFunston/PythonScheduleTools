#!/usr/bin/env python3
# sample regex (^|\D)\d{6}($|\D)
"""Folder and file utilities"""
import re
from os import listdir
from os.path import isfile, isdir, join

def get_file_list(path):
    """Given a path prints a list of all files contained,
    path -- Path that you want to get the file list from
    Returns list of string (file names)"""
    try:
        file_list = [f for f in listdir(path) if isfile(join(path, f))]
        print(file_list)
        return file_list
    except:
        print("Failure")
        return False

def get_folder_list(path):
    """Given a path prints a list of all folders contained,
    path -- Path that you want to get the file list from
    Returns list of string (folder names)"""
    try:
        folder_list = [f for f in listdir(path) if isdir(join(path, f))]
        #print(folder_list)
        return folder_list
    except:
        print("Failure")
        return False

def find_folders(path, name):
    """Returns a list of complete path of a folder if they exists within the given path.
    path -- Path to search
    name -- Partial or complete name to search for
    Returns a list of paths as strings.
    """
    found_folders = list()
    folder_candidates = get_folder_list(path)
    for folder in folder_candidates:
        if name in folder:
            fullpath = path + '/' + folder
            found_folders.append(fullpath)
    return found_folders

#f = get_folder_list("/Volumes/Dockets")
f = find_folders('/Volumes/Dockets', '68')
print(f)