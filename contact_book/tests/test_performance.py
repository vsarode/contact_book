import time
import unittest
from os.path import dirname, abspath

from contact_book.core.contact_functions import insert_data, search_data
from contact_book.src.contacts_trie import Trie


class PerformanceTest(unittest.TestCase):
    '''
      This is tested on i5 machine with 8gb ram
      :return:
    '''

    def setUp(self):
        self.f_name_root = Trie('')
        self.l_name_root = Trie('')

    def test_insert_3lack_less_than_15_sec(self):

        start = time.time()
        path = dirname(
            dirname(abspath(__file__))) + '/assets/contact.txt'
        with open(path, 'r') as input:
            for line in input:
                insert_data(self.f_name_root, self.l_name_root, line.rstrip())
        time_taken = time.time() - start
        print "Insert took: ", time_taken, " Seconds"
        self.assertLess(time_taken, 15)

    def test_search_in_3_lack_contacts_should_be_less_than_10_millisec(self):
        path = dirname(
            dirname(abspath(__file__))) + '/assets/contact.txt'
        with open(path, 'r') as input:
            for line in input:
                insert_data(self.f_name_root, self.l_name_root, line.rstrip())

        start = time.time()
        search_data(self.f_name_root, self.l_name_root, 'Sid')
        time_taken = time.time() - start
        print "Search took: ", time_taken, " Seconds"
        self.assertLess(time_taken, 0.01)


if __name__ == '__main__':
    unittest.main()
