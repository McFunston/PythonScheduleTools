"""Classes related to data collection for job statuses"""
from abc import ABC, abstractmethod
import ExcelReader
import FolderChecker
import CSVReader
class ExcelStatus:
    def __init__(self, source_name, path, id_column, status_column):
        self.path = path
        self.id_column = id_column
        self.status_column = status_column

    def check_status(self, status, job_id):
        return_status = ExcelReader.check_job_status(status, self.path, job_id, self.id_column, self.status_column)
        return return_status

class LogFileStatus:
    def __init__(self, source_name, path, status):
        self.path = path
        self.status = status

    def check_status(self, status, job_id):
        candidates = CSVReader.find_in_csv(self.path, [job_id])
        if candidates: return True
        else: return False

class FileSystemStatus:
    def __init__(self, source_name, path, sub_path, status):
        self.path = path
        self.sub_path = sub_path
        self.status = status

class FileStatus(FileSystemStatus):
    def __init__(self, source_name, path, sub_path, status):
        super().__init__(self, path, sub_path, status)

    def check_status(self, status, job_id):
        folders_to_check = FolderChecker.find_folders(self.path, [job_id])
        folders_to_check = FolderChecker.folder_append(folders_to_check, self.sub_path)
        print_files = FolderChecker.count_files(folders_to_check)
        if print_files: return True
        else: return False

class FolderStatus(FileSystemStatus):

    def __init__(self, source_name, path, sub_path, folder, status):
        super().__init__(self, path, sub_path, status)

    def check_status(self, status, job_id):
        folders_to_check = FolderChecker.find_folders(self.path, [job_id])
        folders_to_check = FolderChecker.folder_append(folders_to_check, self.sub_path)
        for folder in folders_to_check:
            if FolderChecker.folder_exists(folder+folder):
                return True
            else: return False



