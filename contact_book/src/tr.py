def _char_to_index(ch):
    return ord(ch) - ord('a')


class Trie:
    def __init__(self, c):
        self.children = [None] * 26
        self.char = c
        self.s_node = None
        self.isEndOfWord = False

    def add_child(self, ch, index):
        self.children[index] = Trie(ch)
        return self.children[index]

    def insert(self, key):
        if not key:
            self.isEndOfWord = True
            return
        index_to_insert = _char_to_index(key[0])
        if not self.children[index_to_insert]:
            child = self.add_child(key[0], index_to_insert)
        else:
            child = self.children[index_to_insert]
        child.insert(key[1:])

    def get_closure_words(self, pref, node):
        if not node:
            return []
        word = pref + node.char
        if node.isEndOfWord:
            childs = filter(lambda x: x, node.children)
            v = [word]
            for o in childs:
                v.extend(self.get_closure_words(word, o))
            return v
        v = []
        for o in filter(lambda x: x, node.children):
            v.extend(self.get_closure_words(word, o))
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


if __name__ == '__main__':
    n_root = Trie('')
    s_root = Trie('')
    n_root.insert('the')
    n_root.insert('these')
    traverse(n_root)
    last = n_root.search('the')
    print last.__dict__
    print last.get_closure_words('th', last)
