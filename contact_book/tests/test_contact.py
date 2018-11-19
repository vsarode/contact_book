import unittest
from os.path import dirname, abspath
import time
from contact_book.src.trie import Trie, search_data
from contact_book.src.trie import insert_data
from contact_book.utils.performance_measure import timerfunc


class TestContactBook(unittest.TestCase):
    def setUp(self):
        self.f_name_root = Trie('')
        self.l_name_root = Trie('')

    def test_should_insert_first_name_last_name(self):
        self.assertTrue(insert_data(self.f_name_root, self.l_name_root,
                                    'mahadev vyavahare'))

    def test_should_insert_first_name(self):
        self.assertTrue(insert_data(self.f_name_root, self.l_name_root,
                                    'vitthal'))

    def test_should_not_insert_number_as_name(self):
        self.assertFalse(insert_data(self.f_name_root, self.l_name_root,
                                     '123'))
    #
    # def test_insert_time_for_1000_contact(self):
    #     path = dirname(dirname(abspath(__file__))) + '/assets/contacts.txt'
    #     start = time.time()
    #     # import pdb; pdb.set_trace()
    #     with open(path, 'r') as input:
    #         for line in input:
    #             insert_data(self.f_name_root, self.l_name_root, line.rstrip())
    #     time_to_execute = time.time() - start
    #     print "Insert Time took:", time_to_execute


if __name__ == '__main__':
    unittest.main()
