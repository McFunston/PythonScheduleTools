import json
import pprint
import DataSources

DSFFILE = 'DataSources.json'

class DataSourceFactory:

    def __init__(self):
        self.sources = dict()

    def get_sources(self, id_list):
        with open(DSFFILE) as json_file:
            data_sources = json.load(json_file)
            return data_sources

        for id_num in id_list:
            for key, value in data_sources:
                if  'Excel File' in value['Data Type']:
                    source = DataSources.ExcelStatus(data_sources[key])
                if 'CSV Log File' in value['Data Type']:
                    source = DataSources.LogFileStatus(data_sources[key])
                if 'Files' in value['Data Type']:
                    source = DataSources.FileStatus(data_sources[key])
                if 'Folder' in value['Data Type']:
                    source = DataSources.FolderStatus(data_sources[key])
                if 'File Name' in value['Data Type']:
                    source = DataSources.FileStatusByName(data_sources[key])
            self.sources[id_num] = source

        return self.sources



