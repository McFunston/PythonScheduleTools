#!/usr/bin/env python3
"""A single source of data by which to determine the status of a job"""
class DataSource():
    """A single source of data by which to determine the status of a job"""
    def __init__(self, job_id, service, data_source_args):
        self.service = service
        if 'Sub Path' in data_source_args:
            self.path = data_source_args['Path'] + job_id + data_source_args['']
        else:
            self.path = data_source_args['Path']
    