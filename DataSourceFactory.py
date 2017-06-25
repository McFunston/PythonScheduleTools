import json
import DataSources
import pprint
DSFFILE = 'DataSources.json'

class DataSourceFactory:
    
    sources = list()

    def get_sources(self, id_list):
        with open(DSFFILE) as json_file:
            data_sources = json.load(json_file)
            return data_sources
        
        for id in id_list:
            for key, value in data_sources:
                if  'Excel File' in value[0]:
                    source = DataSources.ExcelStatus(key, value[1], value[2], value[3])
                if 'CSV Log File' in value[0]:
                    source = DataSources.LogFileStatus(key, value[1], value[2])
                if 'Files' in value[0]:
                    
            
