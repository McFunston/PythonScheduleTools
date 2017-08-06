#!/usr/bin/env python3
"""A factory for creating data sources"""

def merge_path(job_id, data_source_dict):
    if 'Sub Path' in data_source_dict:
        data_source_dict['Path'] = data_source_dict['Path'] + job_id + data_source_dict['Subpath']
        del data_source_dict['Subpath']
    else:
        data_source_dict['Path'] = data_source_dict['Path']
