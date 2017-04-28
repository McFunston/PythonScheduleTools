from xlrd import open_workbook,XL_CELL_TEXT

def GetJobs(fileName, columns):
    
    book = open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    jobs = list()
    for row_index in range(sheet.nrows-1):
        jn = list()
        for column_index in columns:
            jn.append(sheet.cell(row_index+1, column_index).value.encode("latin-1"))
            jobs.append(jn)    
            print jobs[row_index]

GetJobs('Printflow-ToDo.xls',[3,2])