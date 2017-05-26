#!/usr/bin/env python3
"""Utility to check whether a status listed in an Excel file is correct
by checking for the existance of files (if we have files why hasn't it been statused as "FilesIn"?)
"""
import ExcelReader
import CSVReader
import pprint

def check_status_by_csv(excel_filename, status_column, id_column, status, csv_file):
    jobs_to_check = ExcelReader.get_jobs_by_status(excel_filename, status_column, status)
    jobs_to_check = ExcelReader.get_just_ids(jobs_to_check, id_column)
    candidates = list()
    candidates = CSVReader.find_in_csv(csv_file, jobs_to_check)
    return candidates

#TEST = check_status_by_files('Printflow-ToDo1.xls', 2, 3, 'Files In', 'G:/TestWorkFolder/Dockets', '/Production/Print')
#print(TEST)
#TEST = check_status_by_csv('Printflow-ToDo1.xls', 2, 3, 'Proof Out', 'ProofLog.csv')
#pprint.pprint(TEST)
