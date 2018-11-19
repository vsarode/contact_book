class Trie:
    def __init__(self, c):
        self.children = [None] * 26
        self.char = c
        self.s_node = [None] * 26
        self.is_end_of_word = False

    def add_child(self, ch, index):
        self.children[index] = Trie(ch)
        return self.children[index]

    def insert(self, key):
        if not key:
            self.is_end_of_word = True
            return self
        index_to_insert = _char_to_index(key[0])
        if not self.children[index_to_insert]:
            child = self.add_child(key[0], index_to_insert)
        else:
            child = self.children[index_to_insert]
        return child.insert(key[1:])

    def get_closure_words(self, pref, node, travel_next, is_name):
        if not node:
            return []
        word = pref + node.char
        if node.isEndOfWord:
            childs = filter(lambda x: x, node.children)
            if travel_next:
                s_nodes = filter(lambda x: x, node.s_node)
                surnames = []
                for o in s_nodes:
                    surnames.extend(
                        self.get_closure_words("", o, False, is_name))
                if surnames:
                    if is_name:
                        v = [word + " " + x for x in surnames]
                    else:
                        v = [x + " " + word for x in surnames]
                else:
                    v = [word]
            else:
                v = [word]
            for o in childs:
                v.extend(self.get_closure_words(word, o, travel_next, is_name))
            return v
        v = []
        filtered_childs = filter(lambda x: x, node.children)
        for o in filtered_childs:
            v.extend(self.get_closure_words(word, o, travel_next, is_name))
        return v

    def search(self, key):
        if not key:
            return self
        index_to_insert = _char_to_index(key[0])
        if not self.children[index_to_insert]:
            return None
        child = self.children[index_to_insert]
        return child.search(key[1:])


def _char_to_index(ch):
    if ch.isupper():
        return ord(ch) - ord('A')
    else:
        return ord(ch) - ord('a')


def search_data(f_name_root, l_name_root):
    data = raw_input('Enter name: ')
    f_name_last = f_name_root.search(data)
    l_name_last = l_name_root.search(data)
    # print f_name_last.__dict__
    # print s_last.__dict__
    names = []
    surnames = []
    if f_name_last:
        names = f_name_last.get_closure_words(data[:-1], f_name_last, True,
                                              True)
    print names
    if l_name_last:
        surnames = l_name_last.get_closure_words(data[:-1], l_name_last, True,
                                                 False)
    print surnames
    names.extend(surnames)
    print '\n'.join(names)


def insert_data(f_name_root, l_name_root):
    data = raw_input('Enter name: ')
    try:
        splited_data = data.split(" ")
        name = splited_data[0]
        f_name_last_node = f_name_root.insert(name)

        if len(splited_data) > 1:
            last_name = splited_data[1]
            l_name_last_node = l_name_root.insert(last_name)

            f_name_last_node.s_node[_char_to_index(last_name[0])] = \
                l_name_root.children[
                    _char_to_index(
                        last_name[0])]

            l_name_last_node.s_node[_char_to_index(name[0])] = \
                f_name_root.children[
                    _char_to_index(
                        name[0])]
            # print ""
    except Exception as e:
        # print data
        # print e
        # raise e
        return False
    return True


if __name__ == '__main__':
    n_root = Trie('')
    s_root = Trie('')

    insert_data(n_root, s_root)
    insert_data(n_root, s_root)
    # insert_data(n_root, s_root, "mahadev solapur")
    # insert_data(n_root, s_root, "sopan gaikwad")
    # insert_data(n_root, s_root, "sochin gaikwad")
    # insert_data(n_root, s_root, "vitthal sarode")
    # insert_data(n_root, s_root, "arun kamble")

    search_data(n_root, s_root)

    #
    # n_root.insert('these')
    # traverse(n_root)
    # last = n_root.search('the')
    # print last.__dict__
    # print last.get_closure_words('th', last)
