#!/usr/bin/env python3
# sample regex (^|\D)\d{6}($|\D)
"""Folder and file utilities"""
import re
from os import listdir
from os.path import isfile, isdir, join

def get_file_list(path):
    """Given a path prints a list of all files contained,
    Args: path: Path that you want to get the file list from
    Returns: list of string (file names)"""
    try:
        file_list = [f for f in listdir(path) if isfile(join(path, f))]
        #print(file_list)
        return file_list
    except:
        #print("Failure")
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

def find_folders(path, names):
    """Returns a list of complete path of a folder if they exists within the given path.
    path -- List of paths to search
    name -- Partial or complete name to search for
    Returns a list of paths as strings.
    """
    found_folders = list()
    folder_candidates = get_folder_list(path)
    for name in names:
        for folder in folder_candidates:
            if name in folder:
                fullpath = path + '/' + folder
                found_folders.append(fullpath)
    return found_folders

def folder_append(folders, sub_folder):
    """Appends subfolder paths onto a list of folders
        Args:
            folders: list of folders to append to
            sub_folder: path to append (string)
        Returns: list of folder paths
    """
    full_folder = list()
    for folder in folders:
        folder += sub_folder
        full_folder.append(folder)
    return full_folder

def count_files(folders):
    """Count the files contained in a folder
    Args:
        folder: Path to check
    Returns: [Folder Path, Count of files contained (int), List of files]
    """
    folder_size = list()
    for folder in folders:
        file_list = get_file_list(folder)
        folder_size.append([folder, len(file_list), file_list])
    return folder_size

#f = get_folder_list("/Volumes/Dockets")
#folder_list = find_folders('/Volumes/Dockets', ['689965', '689931'])
#FOLDER_LIST = folder_append(find_folders('G:/TestWorkFolder/Dockets', ['684421', '685543']), "/Production/Print")
#print(FOLDER_LIST)
#FILE_COUNT = count_files(["G:/TestWorkFolder/Dockets/684421/Production/Print"])
#print(FILE_COUNT)
