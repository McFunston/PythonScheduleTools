#!/usr/bin/env python3
"""Tools for extracting job info from CSV files"""
import csv
import pprint
def find_in_csv(file_name, search_string):
    """Find a string within a CSV file
    Args:
        file_name: Name of csv file to search
        search_string: String to be searched for
    Returns: A list of dates and print jobs
    """
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(x.replace('\0', '') for x in csvfile)
        #log_file = csv.reader(csvfile, delimiter=',', quotechar='"')
        findings = [[r[0], r[1]] for r in reader if len(r) > 1 and search_string in r[1]]
        return findings
FOUND = find_in_csv('Job Log.csv', '690137')
pprint.pprint(FOUND)
