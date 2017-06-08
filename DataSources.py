"""Classes related to data collection for job statuses"""
from abc import ABC, abstractmethod
import ExcelReader
import FolderChecker
class ExcelStatus:
    def __init__(self, source_name, path, id_column, status_column):
        self.path = path
        self.id_column = id_column
        self.status_column = status_column

    def check_status(self, status):
        return_status = ExcelReader.get_jobs_by_status(self.path, self.status_column, status)
        return 

class LogFileStatus:
    def __init__(self, source_name, path, status):
        self.path = path
        self.status = status

class FileSystemStatus:
    def __init__(self, source_name, path, sub_path, status):
        self.path = path
        self.sub_path = sub_path
        self.status = status

class FileStatus(FileSystemStatus):
    def __init__(self, source_name, path, sub_path, status):
        super().__init__(self, path, sub_path, status)

class FolderStatus(FileSystemStatus):

    def __init__(self, source_name, path, sub_path, status):
        super().__init__(self, path, sub_path, status)
    

