class ExcelSchedule:
    def __init__(self, path, id_column, status_column):
        self.path = path
        self.id_column = id_column
        self.status_column = status_column

class LogFile:
    def __init__(self, path, status):
        self.path = path
        self.status = status

class storage_folder:
    def __init__(self, path, sub_path, status):
        self.path = path
        self.sub_path = sub_path
        self.status = status

    