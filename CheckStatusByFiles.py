#!/usr/bin/env python3
"""Utility to check whether a status listed in an Excel file is correct
by checking for the existance of files (if we have files why hasn't it been statused as "FilesIn"?)
"""
import ExcelReader
import FolderChecker

def check_status_by_files(excel_filename, status_column, id_column, status, root_path, sub_path):
    jobs_to_check = ExcelReader.get_jobs_by_status(excel_filename, status_column, status)
    jobs_tocheck = ExcelReader.get_just_ids(jobs_to_check, id_column)
    folders_to_check = FolderChecker.find_folders(root_path, jobs_to_check)
    folders_to_check = FolderChecker.folder_append(folders_to_check, sub_path)
    candidates = FolderChecker.count_files(folders_to_check)
    return candidates

TEST = check_status_by_files('Printflow-ToDo.xls', 2, 3, 'Files In', 'G:/TestWorkFolder/Dockets', '/Production/Print')
print(TEST)