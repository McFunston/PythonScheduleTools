#!/usr/bin/env python3
"""MS Excel tools related to schedules save as workbooks"""

from xlrd import open_workbook

class ExcelReader():

    def __init__(self, path, job_id, id_column, date_column, status_column, status):
        self.path = path
        self.id_column = id_column
        self.date_column = date_column
        self.status_column = status_column
        self.status = status
        self.job_id = job_id

    def list_strip(self, list_to_strip):
        """Removes unecessary spaces from a list of cells
        Args:
        list_to_strip: A list of cells
        Returns: A list of strings"""
        stripped_list = [x.value.strip() for x in list_to_strip]
        return stripped_list


    def _get_all_jobs(self, file_name):
        """Get the contents of the first worksheet of an Excel file
        Args:
        file_name: The name of the Excel file containing jobs
        Returns: Excel work sheet as xlrd.sheet.Sheet"""
        try:
            with open_workbook(file_name) as book:
                sheet = book.sheet_by_index(0)
            return sheet
        except FileNotFoundError:
            raise ValueError("That file doesn't exist at the given location")


    def _excel_to_dict(self, file_name):
        sheet = self._get_all_jobs(file_name)
        excel_dict = dict()
        for row_index in range(sheet.nrows - 1):
            for column_index in range(sheet.ncols - 1):
                cell_value = sheet.cell(row_index + 1, column_index + 1).value
                cell_value = cell_value.strip()
                cell_location = (row_index + 1, column_index + 1)
                excel_dict[cell_location] = cell_value
        return excel_dict

    def get_jobs_by_id(self, file_name, id_column, job_id):
        """Gets the rows in a workbook that relate to a given job

        Args:
            file_name: The name of the Excel file containing jobs
            id_column: Column containg job identifier (job#, invoice#, etc)
            job_id: A string to search for that is unique to the job being searched for

        Returns: A list containg the rows that match the job_id"""
        try:
            sheet = self._get_all_jobs(file_name)
        except ValueError as error:
            print(error.args)
            raise
        rows = sheet.get_rows()
        jobs = [self.list_strip(row)
                for row in rows if row[id_column].value == str(job_id)]
        return jobs


    def get_jobs_by_status(self, file_name, status_column, status):
        """Get all of the rows in an Excel file where the status column contains a certain status
        Args:
            file_name: Name of the Excel file
            status_column: Column that contains the statuses for the jobs
            status: Status to filter by
        Returns: A list of row contents
        """
        try:
            sheet = self.get_all_jobs(file_name)
        except ValueError as error:
            print(error.args)
            raise
        rows = sheet.get_rows()
        jobs = [self.list_strip(row)
                for row in rows if status in row[status_column].value]
        return jobs


    def get_just_ids(self, jobs, id_index):
        """Strip away everything except the job ids from a list of jobs and removes duplicates
        Args:
            jobs: A list of jobs
            id_index: Location in the list of the indices
        Returns: A list of job ids (string)
        """
        ids = [job[id_index] for job in jobs]
        ids = list(set(ids))
        return ids


    def get_all_ids(self, path, id_column):
        """Get all job ids from a given Excel File
        Args:
            path: Path to Excel file to get ids from
            id__column: 0 based column that has ids
        Returns: A list of job ids (string)
        """
        all_jobs = self._get_all_jobs(path)
        all_ids = self.get_just_ids(all_jobs, id_column)
        return all_ids


    def get_list(self):
        ids_with_dates = list()
        jobs = self.get_jobs_by_id(self.path, self.id_column, self.job_id)
        for job in jobs:
            if self.status in job[self.status_column]:
                id_and_date = [job[self.date_column], job[self.id_column]]
                ids_with_dates.append(id_and_date)
        return ids_with_dates

er = ExcelReader('TestData/PrintFlow-ToDo.xls', '690152', 3, 0, 2, 'Proof In')
print(er.get_list())
