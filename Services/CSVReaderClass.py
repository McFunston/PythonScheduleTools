#!/usr/bin/env python3
"""Tools for extracting job info from CSV files"""
import csv
import os
import datetime
import time
import ListShaper
import Cache

class CSVReader():

    def __init__(self, path):
        self.path = path

    def get_data(self):
        cache = Cache.Cache()
        return cache.get_list(self.path, self._get_uncached_data)

    def _get_uncached_data(self):

        with open(self.path, newline='', encoding='latin-1', mode='r') as csvfile:
            reader = csv.reader(x.replace('\0', '') for x in csvfile)
            log = [log_items for log_items in reader]

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
        return self.get_data()


# test_csv = CSVReader('ProofLog.csv')
# test1 = test_csv.get_list()

# test2 = test_csv.get_list()