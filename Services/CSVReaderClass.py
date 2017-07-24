#!/usr/bin/env python3
"""Tools for extracting job info from CSV files"""
import csv
import unittest

import ListShaper

class CSVReader():

    def _read_log(self, file_name):

        #csvfile = open(file_name, newline='', encoding='latin-1', mode='r')
        with open(file_name, newline='', encoding='latin-1', mode='r') as csvfile:
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

    def list_jobs(self, file_name):
        log = self._read_log(file_name)
        
        jobs = ListShaper.job_lister(log)
        return jobs

csv_reader = CSVReader()
TEST = csv_reader.find_in_csv("TestData/ProofLog.csv", "690060")
print(TEST)