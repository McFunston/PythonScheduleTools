"""Classes related to data collection for job statuses"""
import unittest
from abc import ABC, abstractmethod

import CSVReader
import ExcelReader
import FolderChecker


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

class FileStatusByName:
    def __init__(self, source_name, path, status):
        self.path = path
        self.source_name = source_name
        self.status = status

    def check_status(self, status, job_id):
        findings = FolderChecker.get_files_containing(self.path, job_id)
        if len(findings) > 0:
            return True

class FileSystemStatus:
    def __init__(self, source_name, path, sub_path, status):
        self.path = path
        self.sub_path = sub_path
        self.status = status
        self.source_name = source_name

class FileStatus(FileSystemStatus):
    def __init__(self, source_name, path, sub_path, status):
        super().__init__(self, path, sub_path, status)

    def check_status(self, status, job_id):
        folders_to_check = FolderChecker.find_folders(self.path, [job_id])
        folders_to_check = FolderChecker.folder_append(folders_to_check, self.sub_path)
        print_files = FolderChecker.count_files(folders_to_check)
        if print_files:
            return True
        else: return False

class FolderStatus(FileSystemStatus):

    def __init__(self, source_name, path, sub_path, folder, status):
        super().__init__(self, path, sub_path, status)
        self.folder = folder

    def check_status(self, status, job_id):
        folders_to_check = FolderChecker.find_folders(self.path, [job_id])
        folders_to_check = FolderChecker.folder_append(folders_to_check, self.sub_path)
        for folder_to_check in folders_to_check:
            if FolderChecker.folder_exists(folder_to_check+self.folder):
                return True
            else: return False

class DataSourceTests(unittest.TestCase):
    """DataSource unit tests"""
    def test_excel_check_status(self):
        #Arrange
        excel_test = ExcelStatus('Prinflow-ToDo', 'Printflow-ToDo1.xls', 3, 2)
        expected = False
        #Act
        actual = excel_test.check_status("Dollco Printing-Proof In", "687556")
        #Assert
        self.assertEqual(actual, expected)

    def test_log_file_status(self):
        #Arange
        expected = False
        log_file_test = LogFileStatus('Proof Log', 'ProofLog.csv', 'Hunt Club-Proof Out')
        #Act
        actual = log_file_test.check_status('Hunt Club-Proof Out', '690331')
        #Assert
        self.assertEqual(actual, expected)

    def test_file_status(self):
        #Arrange
        expected = True
        test_object = FileStatus('P Drive', 'TestData/Dockets', '/Production/Print', 'Files In')
        #Act
        actual = test_object.check_status('Files In', '685543')
        #Assert
        self.assertEqual(actual, expected)

    def test_folder_status(self):
        #Arrange
        expected = True
        test_object = FolderStatus('P Drive', 'TestData/Dockets', '/Production', '/Print', 'Proof In')
        #Act
        actual = test_object.check_status('Proof In', '685543')
        #Assert
        self.assertEqual(actual, expected)

    def test_FileStatusByName(self):
        #Arrange
        expected = True
        test_object = FileStatusByName('Plates Folder','TestData/Dockets/684421/Production/Print', 'Proof In')
        #Act
        actual = test_object.check_status('Files In', 'Test2')
        #Assert
        self.assertEqual(actual, expected)

#test_object = FolderStatus('P Drive', 'TestData/Dockets', '/Production', '/Print', 'Proof In')
#print(test_object.check_status('Files In', '685543'))

if __name__ == '__main__':
    unittest.main()
