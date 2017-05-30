import unittest
import re
from datetime import datetime

def find_earlier(item1, item2):
    item1_date_time = datetime.strptime(item1[0], '%a %b %d %H:%M:%S %Y')
    item2_date_time = datetime.strptime(item2[0], '%a %b %d %H:%M:%S %Y')
    if item1_date_time < item2_date_time:
        return item1
    else: return item2

def results_shaper(self, results, status):
    shaped_results = list()
    jobs = list()
    for result in results:
        r = (re.search(r"\D(\d{6})\D", result[1]))
        jobs.append(r.groups())
    for job in jobs:
        for result in results:
            if job in result[1]:
                None

class MyTest(unittest.TestCase):

    def test_find_earlier(self):
        #Arrange
        item1 = ['Tue May 30 09:15:42 2017', "item1"]
        item2 = ['Wed May 24 15:44:57 2017', "item2"]
        expected = item2
        #Act
        actual = find_earlier(item1, item2)
        #Assert
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()