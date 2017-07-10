#!/usr/bin/env python3
"""Tools for extracting job info from CSV files"""
import csv
import pprint

def read_log(file_name):
    try:
        csvfile = open(file_name, newline='', encoding='latin-1', mode='r')
    except IOError:
        return
    finally:
        csvfile.close
    reader = csv.reader(x.replace('\0', '') for x in csvfile)
    csvfile.close
    return reader

def find_in_csv(file_name, search_strings):
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
        for search_string in search_strings:
            for r in read:
                if len(r) > 1 and str(search_string) in str(r[1]):
                    findings.append([r[0], r[1]])

    return findings
#FOUND = find_in_csv('Job Log.txt', ['888888', '690381'])
#pprint.pprint(FOUND)
#READ = read_log("Job Log.csv")
#print(READ)
