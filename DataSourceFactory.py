import json
import pprint
import DataSources

DSFFILE = 'DataSources.json'

class DataSourceFactory:

    def __init__(self):
        self.sources = dict()

    def get_sources(self, id_list):
        all_sources = {}
        job_sources = {}
        with open(DSFFILE) as json_file:
            data_sources = json.load(json_file)            

        for id_number in id_list:
            for key, value in data_sources.items():
                temp_dict = dict()
                temp_dict[key] = value
                if  'Excel File' in value['Data Type']:
                    source = DataSources.ExcelStatus(value)
                if 'CSV Log File' in value['Data Type']:
                    source = DataSources.LogFileStatus(value)
                if 'Files' in value['Data Type']:
                    source = DataSources.FileStatus(value)
                if 'Folder' in value['Data Type']:
                    source = DataSources.FolderStatus(value)
                if 'File Name' in value['Data Type']:
                    source = DataSources.FileStatusByName(value)
                job_sources[key] = source
            print(id_number)
            all_sources[id_number] = job_sources

        return all_sources

dsf = DataSourceFactory()
id_list = ['687203', '689398']
sources = dsf.get_sources(id_list)
print(sources['687203']['P drive Files - Huntclub'].check_status('Files In','687203'))


