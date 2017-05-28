#!/usr/bin/env python3
# sample regex (^|\D)\d{6}($|\D)
"""Folder and file utilities"""
import re
import os
import os.path
from os import listdir
from os.path import isfile, isdir, join
import time
import unittest

def get_file_list(path):
    """Given a path returns a list of all files contained,
    Args: path: Path that you want to get the file list from
    Returns: list of string (file names)"""
    try:
        file_list = [f for f in listdir(path) if isfile(join(path, f))]
        return file_list
    except FileNotFoundError:
        print("Failure in get_file_list")
        return ["Bad folder structure"]

def get_full_file_list(path):
    """Given a path returns a list of all files contained,
    with full path,
    Args: path: Path that you want to get the file list from
    Returns: list of string (file names)"""
    file_list = list()
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(".pdf")]:
            if filename[0] != ".":
                file_list.append(os.path.join(dirpath, filename))
            #print(os.path.join(dirpath, filename))
    return file_list

def get_file_list_with_date(path):
    file_list = get_full_file_list(path)
    file_list_with_date = []
    for file in file_list:
        if file[0] != ".":
            #file = path + '/' + file
            try:
                file_list_with_date.append([time.ctime(os.path.getmtime(file)), file])
            except FileNotFoundError:
                print(file + " is not a real file")
    return file_list_with_date

def get_folder_list(path):
    """Given a path returns a list of all folders contained,
    path -- Path that you want to get the file list from
    Returns list of string (folder names)"""
    try:
        folder_list = [f for f in listdir(path) if isdir(join(path, f))]
        return folder_list
    except FileNotFoundError:
        print("Failure in get_folder_list" + path)
        return

def find_folders(path, names):
    """Returns a list of the complete paths of folders if they exists within the given path.
    path -- List of paths to search
    names -- List of partial or complete names to search for
    Returns a list of paths as strings.
    """
    found_folders = list()
    folder_candidates = get_folder_list(path)
    if folder_candidates:
        for name in names:
            for folder in folder_candidates:
                if name in folder:
                    fullpath = path + '/' + folder
                    found_folders.append(fullpath)
        return found_folders
    else: return

def folder_append(folders, sub_folder):
    """Appends subfolder paths onto a list of folders
        Args:
            folders: list of folders to append to
            sub_folder: path to append (string)
        Returns: list of folder paths
    """
    full_folder = list()
    if folders:
        for folder in folders:
            folder += sub_folder
            full_folder.append(folder)
        return full_folder
    else: return

def count_files(folders):
    """Count the files contained in a folder
    Args:
        folder: Path to check
    Returns: [Folder Path, Count of files contained (int), List of files]
    """
    folder_size = list()
    if folders:
        for folder in folders:
            file_list = get_file_list(folder)
            if file_list:
                folder_size.append([folder, len(file_list), file_list])

        return folder_size
    else: return

def folder_exists(folder):
    """Check it a folder exists at a given path
    Args:
        folder: Path of folder to check
    Returns: True if folder exists, False if it doesn't
"""
    if os.path.exists(folder):
        return True
    else:
        return False

class MyTest(unittest.TestCase):
    """FolderChecker.py Unit Tests"""

    def test_get_file_list(self):
        """get_file_list unit test"""
        #Arrange
        expected = ['test.pdf']
        #Act
        actual = get_file_list('TestData/Dockets/685543/Production/print')
        #Assert
        self.assertEqual(actual, expected)

    def test_get_full_file_list(self):
        """get_full_file_list unit test"""
        #Arrange
        expected = ['TestData/Dockets/685543/Production/print\\test.pdf']
        #Act
        actual = get_full_file_list('TestData/Dockets/685543/Production/print')
        #Assert
        self.assertEqual(actual, expected)

    def test_get_file_list_with_date(self):
        #Arrange
        expected = [['Sun May  7 10:06:02 2017', 'TestData/Dockets/685543/Production/print\\test.pdf']]
        #Act
        actual = get_file_list_with_date('TestData/Dockets/685543/Production/print')
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

#f = get_file_list_with_date("/Volumes/share/")
#print(f)
#folder_list = find_folders('/Volumes/Dockets', ['689965', '689931'])
#FOLDER_LIST = folder_append(find_folders('G:/TestWorkFolder/Dockets', ['684421', '685543']), "/Production/Print")
#print(FOLDER_LIST)
#FILE_COUNT = count_files(["G:/TestWorkFolder/Dockets/684421/Production/Print"])
#print(FILE_COUNT)

