#!/usr/bin/env python3
"""A factory for creating a checker/reader object for a data source"""
import Services.FileReader
import Services.CSVReader
import Services.ExcelReader
import Services.FolderReader

def create_service(data_source):
    source = data_source['Data Type']
    if source == 'Files' or source == 'File Name':
        service = Services.FileReader.FileReader(data_source)
    if source == 'Excel File':
        service = Services.ExcelReader.ExcelReader(data_source)
    if source == 'CSV Log File':
        service = Services.CSVReader.CSVReader(data_source)
    if source == 'Folder':
        service = Services.FolderReader.FolderReader(data_source)
    return service
