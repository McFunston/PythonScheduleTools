#!/usr/bin/env python3
"""A single source of data by which to determine the status of a job"""
class DataSource():
    """A single source of data by which to determine the status of a job"""
    def __init__(self, service, data_source_args):
        self.service = service
        self.data_source_args = data_source_args
    