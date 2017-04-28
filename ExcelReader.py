from xlrd import open_workbook,XL_CELL_TEXT

def GetJobs(file):
    book = open_workbook(file)
    sheet = book.sheet_by_index(0)
    jobs = list()
    for row_index in range(sheet.nrows-1):
        jn = list()
        jn.append(sheet.cell(row_index+1, 3).value.encode("latin-1"))
        jn.append(sheet.cell(row_index+1, 2).value.encode("latin-1"))
        jobs.append(jn)    
        print jobs[row_index]

GetJobs('Printflow-ToDo.xls')