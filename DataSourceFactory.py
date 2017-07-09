import json
import pprint
import DataSources

DSFFILE = 'TestData/TestDataSources.json'

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
            #print(id_number)
            all_sources[id_number] = job_sources

        return all_sources

dsf = DataSourceFactory()
id_list = ['687203', '689398', '690714', '684396']
sources = dsf.get_sources(id_list)
print(sources['687203']['P drive Files - Huntclub'].check_status('Files In', '685543'))
print(sources['689398']['P drive Files - Huntclub'].check_status('Files In', '689398'))

print(sources['690714']['PDF Proof Out - Huntclub'].check_status('PDF Proof Out', '690714'))
print(sources['684396']['Xerox Proof Out - Huntclub'].check_status('Proof Out', '684396'))
