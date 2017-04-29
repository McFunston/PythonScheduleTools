from xlrd import open_workbook

def get_jobs(file_name, columns):
    """Print a list of jobs columns from an Excel File"""
    book = open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    jobs_info = list()
    for row_index in range(sheet.nrows-1):
        job_info = list()
        for column_index in columns:
            cell_value = sheet.cell(row_index+1, column_index).value
            cell_value = cell_value.strip()
            job_info.append(cell_value)
        jobs_info.append(job_info)
        print (jobs_info[row_index])

get_jobs('Printflow-ToDo.xls', [3, 2, 7])
