#!/usr/bin/env python3
"""A utility to add any new files in a given folder to a comma separated text file"""
import sys
import csv
import CSVReader
import FolderChecker
def folder_watcher(folder, logfile):
    files = FolderChecker.get_file_list_with_date(folder)
    try:
        file = open(logfile, 'r')
    except IOError:
        file = open(logfile, 'w')
        print ("ruh roh")
    finally:
        file.close()
    current_log = CSVReader.read_log(logfile)
    log = list()
    log = [[l[0], l[1]] for l in current_log]
    files_to_add = list()
    for file in files:
        if file not in log:
            log.append(file)
    #log.append(files_to_add)
    with open(logfile, 'w', newline='', encoding='latin-1') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for file_to_add in log:
            writer.writerow(file_to_add)

#folder_watcher("/Volumes/PTDATA/PDFs", "ProofLog.csv")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Arguments 'folder' and 'logfile' required")
    else:
        folder_watcher(sys.argv[1], sys.argv[2])

