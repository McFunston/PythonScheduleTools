import unittest
import re
from datetime import datetime

def find_earlier(item1, item2):
    item1_date_time = datetime.strptime(item1[0], '%a %b %d %H:%M:%S %Y')
    item2_date_time = datetime.strptime(item2[0], '%a %b %d %H:%M:%S %Y')
    if item1_date_time < item2_date_time:
        return item1
    else: return item2

def job_lister(results):
    shaped_results = list()
    jobs = list()
    found_jobs = list()
    for result in results:
        r = (re.search(r"(\d{6})", result[1]))
        jobs.append(r.groups())
    for job in jobs:
        found_jobs.append(job[0])
    return found_jobs

def job_counter(jobs_list, job_number):
    formed_job = list()
    formed_job.append(job_number)
    formed_job.append(0)
    for job in jobs_list:
        if job_number in job[1]:
            formed_job[1] += 1
            formed_job.append(job[1])
    return formed_job
    
class MyTest(unittest.TestCase):
    item1 = ['Tue May 30 09:15:42 2017', "item1r684500"]
    item2 = ['Wed May 24 15:44:57 2017', "700000item2"]
    items = list()
    items.append(item1)
    items.append(item2)

    def test_find_earlier(self):
        #Arrange

        expected = self.item2
        #Act
        actual = find_earlier(self.item1, self.item2)
        #Assert
        self.assertEqual(actual, expected)

    def test_job_lister(self):
        #Arrange
        expected = ["684500", "700000"]
        #Act
        actual = job_lister(self.items)
        #Assert
        self.assertEqual(actual, expected)

    def test_job_counter(self):
        #Arrange
        expected = ["684500", 1, "item1r684500"]
        #Act
        actual = job_counter(self.items, "684500")
        #Assert
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()