#!/usr/bin/env python3
"""A utility to add any new files in a given folder to a comma separated text file"""
import FolderChecker
def folder_watcher(folder, logfile):
    files = FolderChecker.get_file_list(folder)
    
    try:
        file = open(logfile, 'r')
    except IOError:
        file = open(logfile, 'w')
    finally:
        file.close()

    with open(logfile, mode='r') as logged:
        current_log = logged.read()
    current_log += str(files)
    current_log = str(current_log)
    current_log = current_log.split(',')
    current_log = str(set(current_log))
    with open(logfile, mode='w') as logged:
        logged.write(current_log)
folder_watcher("/", "Proofs.txt")
