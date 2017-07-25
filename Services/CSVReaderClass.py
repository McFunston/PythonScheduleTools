#!/usr/bin/env python3
"""Tools for extracting job info from CSV files"""
import csv
import os
import datetime
import time
import ListShaper

class CSVReader():

    _csv_cache = {}
    _cache_date = {}

    def __init__(self, path):
        self.path = path

    def _check_cache(self):
        if self.path in CSVReader._csv_cache:
            file_date = datetime.datetime.fromtimestamp(os.path.getmtime(self.path))
            cache_cutoff = datetime.datetime.now() - datetime.timedelta(minutes=15)
            if file_date > cache_cutoff:                
                return True

    def _read_log(self):

        if not self._check_cache():

            print ('Did not use cache')

            with open(self.path, newline='', encoding='latin-1', mode='r') as csvfile:
                reader = csv.reader(x.replace('\0', '') for x in csvfile)
                log = [log_items for log_items in reader]
            CSVReader._csv_cache[self.path] = log
            CSVReader._cache_date[self.path] = datetime.datetime.now()
            
        else:
            print ('Used cache')
            log = CSVReader._csv_cache[self.path]

        return log

    def find_in_csv(self, file_name, search_string):
        """Find a string within a CSV file
        Args:
            file_name: Name of csv file to search
            search_string: String to be searched for
        Returns: A list of dates and print jobs
        """
        with open(file_name, newline='', encoding='latin-1') as csvfile:
            reader = csv.reader(x.replace('\0', '') for x in csvfile)
            findings = list()
            read = [r for r in reader]
           
            for r in read:
                if len(r) > 1 and str(search_string) in str(r[1]):
                    findings.append([r[0], r[1]])

        return findings

    def get_list(self):
        return self._read_log()


test_csv = CSVReader('ProofLog.csv')
test1 = test_csv.get_list()
test2 = test_csv.get_list()