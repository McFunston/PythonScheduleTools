import sys
import os.path
import time
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1


def PDFFormChecker(path, fieldName, trueValue):
    #filename = sys.argv[1]
    if 'approved' in path.lower():
        return time.ctime(os.path.getmtime(path))
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    fields = resolve1(doc.catalog['AcroForm'])['Fields']
    for i in fields:
        field = resolve1(i)
        name, value = field.get('T'), field.get('V')
        if fieldName in str(name) and trueValue in str(value):
            return time.ctime(os.path.getmtime(path))
    return False

print(PDFFormChecker('G:/OneDrive/P001R10-Ott3_01.pdf', 'PROOF OK AS SUBMITTED', 'Yes'))
