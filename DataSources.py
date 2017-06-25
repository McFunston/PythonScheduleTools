"""Classes related to data collection for job statuses
All classes must share the folowing interface:
self.source_name (property)
self.check_status(self, status, job_id) (method)"""
import unittest
#from abc import ABC, abstractmethod

import CSVReader
import ExcelReader
import FolderChecker


class ExcelStatus:
    """Data source in which the status is derived from an Excel file."""
    #def __init__(self, source_name, path, id_column, status_column):
    def __init__(self, data_source_dictionary):
        self.source_name = data_source_dictionary['Source Name']
        self.path = data_source_dictionary['Path']
        self.id_column = data_source_dictionary['Id Column']
        self.status_column = data_source_dictionary['Status Column']

    def check_status(self, status, job_id):
        """Check whether a given status is True. Required as part of interface"""
        return_status = ExcelReader.check_job_status(status, self.path, job_id, self.id_column, self.status_column)
        return return_status

class LogFileStatus:
    """Data source in which the status is derived from a comma delimited log file"""
    def __init__(self, source_name, path, status):
        self.path = path
        self.status = status

    def check_status(self, status, job_id):
        """Check whether a given status is true. Required as part of interface"""
        candidates = CSVReader.find_in_csv(self.path, [job_id])
        if candidates: return True
        else: return False

class FileStatusByName:
    """Data source in which the status is derived from the existence of
    files in a given folder which contain the job id in their name
    (ie does a certain folder contain files containing 687254)"""
    def __init__(self, source_name, path, status):
        self.path = path
        self.source_name = source_name
        self.status = status

    def check_status(self, status, job_id):
        """Check whether a given status is true. Required as part of interface"""
        findings = FolderChecker.get_files_containing(self.path, job_id)
        if len(findings) > 0:
            return True

class FileSystemStatus:
    """Abstract class for file or folder based statuses in which the path is
    /static_path/path_containing_job_id/static_subpath (the job folders are
    always contained in a given folder (/dockets for example) and always
    contain a given subfolder (/Production/Print for ex))"""
    def __init__(self, source_name, path, sub_path, status):
        self.path = path
        self.sub_path = sub_path
        self.status = status
        self.source_name = source_name

class FileStatus(FileSystemStatus):
    """Data source in which the status is derived from the existence of files within a
    given root path, variable path containg a string, and a given sub path.
    (ie /Dockets/*variable*/files contains files so the status should be "Files In")"""
    def __init__(self, source_name, path, sub_path, status):
        super().__init__(self, path, sub_path, status)

    def check_status(self, status, job_id):
        """Check whether a given status is true. Required as part of interface"""
        folders_to_check = FolderChecker.find_folders(self.path, [job_id])
        folders_to_check = FolderChecker.folder_append(folders_to_check, self.sub_path)
        print_files = FolderChecker.count_files(folders_to_check)
        if print_files:
            return True
        else: return False

class FolderStatus(FileSystemStatus):
    """Data source in which the status is derived from the existence of a folder within a
    given root path, variable path containg a string, and a given sub path.
    (ie /Prinect Jobs/*variable*/Sequences contains a plating folder so the
    status should be "Proof In")"""

    def __init__(self, source_name, path, sub_path, folder, status):
        super().__init__(self, path, sub_path, status)
        self.folder = folder

    def check_status(self, status, job_id):
        """Check whether a given status is true. Required as part of interface"""
        folders_to_check = FolderChecker.find_folders(self.path, [job_id])
        folders_to_check = FolderChecker.folder_append(folders_to_check, self.sub_path)
        for folder_to_check in folders_to_check:
            if FolderChecker.folder_exists(folder_to_check+self.folder):
                return True
            else: return False

class DataSourceTests(unittest.TestCase):
    """DataSource unit tests"""
    def test_excel_check_status(self):
        """Check that class implements check_status properly"""
        #Arrange
        test_dictionary = {'Source Name': 'Test',
                           'Path': 'Printflow-ToDo1.xls',
                           'Id Column': 3,
                           'Status Column': 2}
        excel_test = ExcelStatus(test_dictionary)
        expected = True
        #Act
        actual = excel_test.check_status('Dollco Printing-Proof In', '687583')
        #Assert
        self.assertEqual(actual, expected)

    def test_log_file_status(self):
        """Check that class implements check_status properly"""
        #Arange
        expected = False
        log_file_test = LogFileStatus('Proof Log', 'ProofLog.csv', 'Hunt Club-Proof Out')
        #Act
        actual = log_file_test.check_status('Hunt Club-Proof Out', '690331')
        #Assert
        self.assertEqual(actual, expected)

    def test_file_status(self):
        """Check that class implements check_status properly"""
        #Arrange
        expected = True
        test_object = FileStatus('P Drive', 'TestData/Dockets', '/Production/Print', 'Files In')
        #Act
        actual = test_object.check_status('Files In', '685543')
        #Assert
        self.assertEqual(actual, expected)

    def test_folder_status(self):
        """Check that class implements check_status properly"""
        #Arrange
        expected = True
        test_object = FolderStatus('P Drive', 'TestData/Dockets', '/Production', '/Print', 'Proof In')
        #Act
        actual = test_object.check_status('Proof In', '685543')
        #Assert
        self.assertEqual(actual, expected)

    def test_file_status_by_name(self):
        """Check that class implements check_status properly"""
        #Arrange
        expected = True
        test_object = FileStatusByName('Plates Folder', 'TestData/Dockets/684421/Production/Print', 'Proof In')
        #Act
        actual = test_object.check_status('Files In', 'Test2')
        #Assert
        self.assertEqual(actual, expected)

#test_object = FolderStatus('P Drive', 'TestData/Dockets', '/Production', '/Print', 'Proof In')
#print(test_object.check_status('Files In', '685543'))

if __name__ == '__main__':
    unittest.main()
