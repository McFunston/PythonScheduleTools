#!/usr/bin/env python3
"""MS Excel tools related to schedules save as workbooks"""
from xlrd import open_workbook

def get_jobs(file_name, columns):
    """Print a list of jobs columns from an Excel File.

    Args:
        file_name: The name of the Excel file containing jobs
        columns: A list of the column indices to get

    Returns: None """
    with open_workbook(file_name) as book:
        sheet = book.sheet_by_index(0)
    jobs_info = list()
    for row_index in range(sheet.nrows-1):
        job_info = list()
        for column_index in columns:
            cell_value = sheet.cell(row_index+1, column_index).value
            cell_value = cell_value.strip()
            job_info.append(cell_value)
        jobs_info.append(job_info)
        print(jobs_info[row_index])

def get_job(file_name, column, job_id):
    """Gets the rows in a workbook that relate to a given job

    Args:
        file_name: The name of the Excel file containing jobs
        columns: A list of the column indices to get
        job_id: A string to search for that is unique to the job being searched for

    Returns: A tuple containg the rows that match the job_id"""

get_jobs('Printflow-ToDo.xls', [0, 3, 2, 7])
