import sys
import unittest
from StringIO import StringIO

from contact_book.core.contact_functions import char_to_index, search_data, \
    get_first_name_last_name_combinations
from contact_book.src.contacts_trie import Trie
from contact_book.src.contacts_trie import insert_data


class TestContactFunctions(unittest.TestCase):
    def setUp(self):
        self.f_name_root = Trie('')
        self.l_name_root = Trie('')

    def test_char_to_index_should_return_0_for_a(self):
        self.assertEqual(char_to_index('a'), 0)

    def test_char_to_index_should_return_0_for_A(self):
        self.assertEqual(char_to_index('A'), 0)

    def test_char_to_index_should_return_none_for_non_alpha_value(self):
        self.assertEqual(char_to_index('1'), None)

    def test_insert_data_should_insert_contact_with_first_name(self):
        self.assertTrue(insert_data(self.f_name_root, self.l_name_root, "help"))

    def test_insert_data_should_insert_contact_with_first_name_and_last_name(
            self):
        self.assertTrue(insert_data(self.f_name_root, self.l_name_root,
                                    "help shift"))

    def test_insert_data_should_not_insert_contact_with_non_alphabet(self):
        self.assertFalse(insert_data(self.f_name_root, self.l_name_root, "13"))

    def test_insert_data_should_not_insert_duplicate_contact(self):
        insert_data(self.f_name_root, self.l_name_root, "help")
        self.assertFalse(insert_data(self.f_name_root, self.l_name_root,
                                     "help"))

    def test_insert_data_should_print_error_msg_for_duplicate_contact(
            self):
        insert_data(self.f_name_root, self.l_name_root, "help")
        self.assertFalse(insert_data(self.f_name_root, self.l_name_root,
                                     "help"))

    def test_search_data_should_search_by_first_name(self):
        insert_data(self.f_name_root, self.l_name_root, "help")
        insert_data(self.f_name_root, self.l_name_root, "help shift")
        out = StringIO()
        sys.stdout = out
        search_data(self.f_name_root, self.l_name_root, 'he')
        output = out.getvalue().strip()
        self.assertEqual(output, 'help\nhelp shift')

    def test_search_data_should_search_by_last_name(self):
        insert_data(self.f_name_root, self.l_name_root, "help")
        insert_data(self.f_name_root, self.l_name_root, "help shift")
        out = StringIO()
        sys.stdout = out
        search_data(self.f_name_root, self.l_name_root, 'sh')
        output = out.getvalue().strip()
        self.assertEqual(output, 'help shift')

    def test_search_data_should_search_should_give_result_in_insertion_order(
            self):
        insert_data(self.f_name_root, self.l_name_root, "help shift")
        insert_data(self.f_name_root, self.l_name_root, "help")
        out = StringIO()
        sys.stdout = out
        search_data(self.f_name_root, self.l_name_root, 'he')
        output = out.getvalue().strip()
        self.assertEqual(output, 'help shift\nhelp')

    def test_search_data_should_exact_search_should_give_first_names_contact_first(
            self):
        insert_data(self.f_name_root, self.l_name_root, "help")
        insert_data(self.f_name_root, self.l_name_root, "help shift")
        out = StringIO()
        sys.stdout = out
        search_data(self.f_name_root, self.l_name_root, 'he')
        output = out.getvalue().strip()
        self.assertEqual(output, 'help\nhelp shift')

    def test_search_data_should_print_empty_for_wrong_search_key(self):
        insert_data(self.f_name_root, self.l_name_root, "help")
        insert_data(self.f_name_root, self.l_name_root, "help shift")
        out = StringIO()
        sys.stdout = out
        search_data(self.f_name_root, self.l_name_root, 'vi')
        output = out.getvalue().strip()
        self.assertEqual(output, '')

    def test_search_data_happy(self):
        insert_data(self.f_name_root, self.l_name_root, "help")
        insert_data(self.f_name_root, self.l_name_root, "help shift")
        out = StringIO()
        sys.stdout = out
        search_data(self.f_name_root, self.l_name_root, 'he')
        output = out.getvalue().strip()
        self.assertEqual(output, 'help\nhelp shift')

    def test_get_first_name_last_name_combinations_should_give_names_list(self):
        insert_data(self.f_name_root, self.l_name_root, "a")
        insert_data(self.f_name_root, self.l_name_root, "a b")

        node = self.f_name_root.children[0]
        self.assertEqual(get_first_name_last_name_combinations(node, 'a',
                                                               True), ['a',
                                                                       'a b'])


if __name__ == '__main__':
    unittest.main()
