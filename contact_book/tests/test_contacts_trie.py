import unittest

from contact_book.src.contacts_trie import Trie
from contact_book.src.contacts_trie import insert_data


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
        self.assertFalse(insert_data(self.f_name_root, self.l_name_root, '123'))

    def test_add_child_should_add_alphabet(self):
        node = self.f_name_root.add_child('a', 0)
        self.assertIsInstance(node, Trie)

    def test_add_child_should_not_add_number(self):
        node = self.f_name_root.add_child('1', 0)
        self.assertEqual(node, None)

    def test_insert_should_return_node_after_key_insertion(self):
        node = self.f_name_root.insert('help')
        self.assertIsInstance(node, Trie)

    def test_insert_should_return_is_end_of_word_true_after_successfull_insertion(
            self):
        node = self.f_name_root.insert('shift')
        self.assertTrue(node.is_end_of_word)

    def test_insert_should_insert_a_at_0_index(self):
        self.f_name_root.insert("a")
        self.assertEqual(self.f_name_root.children[0].char, 'a')

    def test_insert_returned_nodes_end_of_word_should_be_true(self):
        node = self.f_name_root.insert("a")
        self.assertTrue(node.is_end_of_word)

    def test_after_insert_two_char_returned_nodes_parenst_end_of_word_should_be_false(
            self):
        self.f_name_root.insert("ab")
        self.assertFalse(self.f_name_root.is_end_of_word)

    def test_get_closure_words_should_return_list_of_contacts_for_given_node(
            self):
        self.f_name_root.insert('help')
        self.f_name_root.insert('helpshift')
        self.assertEqual(self.f_name_root.get_closure_words('',
                                                            self.f_name_root,
                                                            True),
                         ['help', 'helpshift'])

    def test_get_closure_words_should_return_empty_list_for_none_node(self):
        self.assertEqual(self.f_name_root.get_closure_words('', None, True), [])


if __name__ == '__main__':
    unittest.main()
