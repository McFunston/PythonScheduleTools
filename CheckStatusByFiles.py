#!/usr/bin/env python3
"""Utility to check whether a status listed in an Excel file is correct
by checking for the existance of files (if we have files why hasn't it been statused as "FilesIn"?)
"""
import ExcelReader
import FolderChecker

def check_status_by_files(excel_filename, status_column, id_column, status, root_path, sub_path):
    jobs_to_check = ExcelReader.get_jobs_by_status(excel_filename, status_column, status)
    status_suspects = 