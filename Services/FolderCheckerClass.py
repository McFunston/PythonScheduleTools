#!/usr/bin/env python3
# sample regex (^|\D)\d{6}($|\D)
"""Folder and file utilities"""

import os
import os.path
from os import listdir
from os.path import isfile, isdir, join
import time


class FolderChecker():

    def __init__(self, path):
        self.path = path

    def _get_full_file_list(self):
        """Given a path returns a list of all files contained,
        with full path,
        Args: path: Path that you want to get the file list from
        Returns: list of string (file names)"""
        file_list = [join(self.path, f) for f in listdir(
            self.path) if isfile(join(self.path, f)) and f[0] != "."]
        return file_list

    def get_file_list(self):
        """Given a path, returns a list of dates and file paths
        Args: path: Path that you want to get the file list from
        Returns: list of [date, path]
        """
        file_list = self._get_full_file_list()
        file_list_with_date = list()
        for file in file_list:
            if file[0] != ".":
                try:
                    file_with_date = [time.ctime(
                        os.path.getmtime(file)), os.path.basename(file)]
                    file_list_with_date.append(file_with_date)
                except FileNotFoundError:
                    print(file + " is not a real file")
        return file_list_with_date

    def get_folder_list(self):
        """Given a path, returns a list of dates and folders
        Args: path: Path that you want to get the file list from
        Returns: list of [date, foldernames]
        """
        folder_list_with_date = list()
        folder_list = [f for f in listdir(self.path) if isdir(join(self.path, f))]
        for folder in folder_list:
            folder_with_date = [time.ctime(
                os.path.getmtime(self.path + '/' + folder)), folder]
            folder_list_with_date.append(folder_with_date)
        return folder_list_with_date

    def _find_folders(self, names):
        """Returns a list of the complete paths of folders if they exists within the given path.
        path -- List of paths to search
        names -- List of partial or complete names to search for
        Returns a list of paths as strings.
        """
        found_folders = list()
        folder_candidates = self.get_folder_list()
        if folder_candidates:
            for name in names:
                for folder in folder_candidates:
                    if name in folder:
                        fullpath = self.path + '/' + folder
                        found_folders.append(fullpath)
            return found_folders
        else:
            return

    def _folder_append(self, folders, sub_folder):
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
        else:
            return

    def _folder_exists(self, folder):
        """Check it a folder exists at a given path
        Args:
            folder: Path of folder to check
        Returns: True if folder exists, False if it doesn't
    """
        if os.path.exists(folder):
            return True
        else:
            return False

# fc = FolderChecker('TestData')
# print(fc.get_folder_list())