from contact_book.core.contact_functions import insert_data, search_data, \
    char_to_index, get_first_name_last_name_combinations


class Trie:
    '''
        Trie to make searching faster
    '''

    def __init__(self, c):
        '''
        Constructor for trie node
        :param c: character to be store at node
        '''

        self.children = [None] * 26
        self.char = c
        self.s_node = [None] * 26
        self.is_end_of_word = False
        self.name_or_surname = []

    def add_child(self, ch, index):
        '''
        To add child into trie
        :param ch:
        :param index:
        :return: trie node
        '''
        if not ch.isalpha():
            return None
        self.children[index] = Trie(ch)
        return self.children[index]

    def insert(self, key):
        '''
        Insert key by traversing trie
        :param key: Contact to be inserted into trie
        :return: trie node
        '''
        if not key:
            self.is_end_of_word = True
            return self
        index_to_insert = char_to_index(key[0])
        if not self.children[index_to_insert]:
            child = self.add_child(key[0], index_to_insert)
        else:
            child = self.children[index_to_insert]
        return child.insert(key[1:])

    def get_closure_words(self, prefix, node, is_first_name):
        '''
        To get the closure for the search keys last words child nodes
        :param prefix: Prefix for every contact
        :param node: Last node of search key to get closure
        :param is_first_name: To check key is first name of last name
        :return: List of closure of the first name or last name
        '''
        if not node:
            return []
        name = prefix + node.char
        if node.is_end_of_word:
            childs = filter(lambda x: x, node.children)
            v = get_first_name_last_name_combinations(node, name, is_first_name)
            for o in childs:
                v.extend(self.get_closure_words(name, o, is_first_name))
            return v
        v = []
        filtered_childs = filter(lambda x: x, node.children)
        for o in filtered_childs:
            v.extend(self.get_closure_words(name, o, is_first_name))
        return v

    def search(self, key):
        '''
        To get the node for the keys last alphabet
        :param key: Query to search
        :return: Keys last alphabets node (i.e. Trie node)
        '''

        if not key:
            return self
        index_to_insert = char_to_index(key[0])
        if not self.children[index_to_insert]:
            return None
        child = self.children[index_to_insert]
        return child.search(key[1:])
