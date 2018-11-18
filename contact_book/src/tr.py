def _char_to_index(ch):
    return ord(ch) - ord('a')


class Trie:
    def __init__(self, c):
        self.children = [None] * 26
        self.char = c
        self.s_node = [None] * 26
        self.isEndOfWord = False

    def add_child(self, ch, index):
        self.children[index] = Trie(ch)
        return self.children[index]

    def insertSname(self, key):
        if not key:
            self.isEndOfWord = True
            return
        index_to_insert = _char_to_index(key[0])
        if not self.children[index_to_insert]:
            child = self.add_child(key[0], index_to_insert)
        else:
            child = self.children[index_to_insert]
        child.insert(key[1:])

    def insert(self, key):
        if not key:
            self.isEndOfWord = True
            return self
        index_to_insert = _char_to_index(key[0])
        if not self.children[index_to_insert]:
            child = self.add_child(key[0], index_to_insert)
        else:
            child = self.children[index_to_insert]
        return child.insert(key[1:])

    def get_closure_words(self, pref, node, travelNext, is_name):
        if not node:
            return []
        word = pref + node.char
        if node.isEndOfWord:
            childs = filter(lambda x: x, node.children)
            if travelNext:
                s_nodes = filter(lambda x: x, node.s_node)
                surnames = []
                for o in s_nodes:
                    surnames.extend(
                        self.get_closure_words("", o, False, is_name))
                if is_name:
                    v = [word + " " + x for x in surnames]
                else:
                    v = [x + " " + word for x in surnames]
            else:
                v = [word]
            for o in childs:
                v.extend(self.get_closure_words(word, o, travelNext, is_name))
            return v
        v = []
        filtedred_childs = filter(lambda x: x, node.children)
        for o in filtedred_childs:
            v.extend(self.get_closure_words(word, o, travelNext, is_name))
        return v

    def search(self, key):
        if not key:
            return self
        index_to_insert = _char_to_index(key[0])
        if not self.children[index_to_insert]:
            return None
        child = self.children[index_to_insert]
        return child.search(key[1:])


def traverse(root):
    if root == None:
        return
    print root.char
    if root.isEndOfWord:
        print "---------"
    for o in root.children:
        traverse(o)


def search_data(n_root, s_root, data):
    n_last = n_root.search(data)
    s_last = s_root.search(data)
    # print n_last.__dict__
    # print s_last.__dict__
    names = []
    surnames = []
    if n_last:
        names = n_last.get_closure_words(data[:-1], n_last, True, True)
    # print names
    if s_last:
        surnames = s_last.get_closure_words(data[:-1], s_last, True, False)

    names.extend(surnames)
    print names


def insertData(n_root, s_root, data):
    name = data.split(" ")[0]
    nlastNode = n_root.insert(name)
    last_name = data.split(" ")[1]

    slastNode = s_root.insert(last_name)

    nlastNode.s_node[_char_to_index(name[-1])] = s_root.children[
        _char_to_index(
            last_name[0])]

    slastNode.s_node[_char_to_index(last_name[-1])] = n_root.children[
        _char_to_index(
            name[0])]


if __name__ == '__main__':
    n_root = Trie('')
    s_root = Trie('')
    insertData(n_root, s_root, "mahadev vyavahare")
    insertData(n_root, s_root, "mahadev solapur")
    insertData(n_root, s_root, "sopan gaikwad")
    insertData(n_root, s_root, "sochin gaikwad")
    insertData(n_root, s_root, "vitthal sarode")
    insertData(n_root, s_root, "arun kamble")
    search_data(n_root, s_root, 'mahadev')

    #
    # n_root.insert('these')
    # traverse(n_root)
    # last = n_root.search('the')
    # print last.__dict__
    # print last.get_closure_words('th', last)
