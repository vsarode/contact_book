# Python program for insert and search
# operation in a Trie

class TrieNode:

    # Trie node class
    def __init__(self, c):
        self.children = [None] * 26
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
        self.char = c


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = None

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):
        if self.root == None:
            self.root = TrieNode('Z')
        if len(key) == 0:
            self.root.isEndOfWord = True
            return self.root

        indexToInsert = self._charToIndex(key[0])
        node = TrieNode(key[0])
        if not self.root.children[indexToInsert]:
            self.root.children[indexToInsert] = node
        rem = key[1:]
        self.root=self.root.children[indexToInsert]
        self.insert(rem)
        return self.root

    def search(self, root, key):
        index = self._charToIndex(key[0])
        node = root.children[index]
        return self.someS(0, key)

    def someS(self, index, key):
        if index == len(key) - 1 and key[index] == self.root.char:
            return self.root
        if index > len(key) or key[index] != self.root.char:
            return None
        nodeIndex = self._charToIndex(key[index+1])
        self.root= self.root.children[nodeIndex]
        return self.someS(index + 1, key)

    # def search(self, key):
    #     # pCrawl = self.root
    #     length = len(key)
    #     for level in range(length - 1):
    #         if pCrawl.char == key[level]:
    #             pCrawl = pCrawl.children[self._charToIndex(key[level + 1])]
    #         else:
    #             return None
    #     if pCrawl.char == key[length - 1]:
    #         return pCrawl
    #     return None


# driver function


def charIndex(c):
    return ord(c) - ord('a')


def traverse(root):
    if root == None:
        return
    print root.char
    if root.isEndOfWord:
        print "---------"
    for o in root.children:
        traverse(o)


def build_tree():
    # import pdb; pdb.set_trace()
    t = Trie()
    t.root = t.insert("the")

    # t.insert(t.root, "there")
    # t.insert(t.root, "thedon")
    #
    #
    # t.insert(t.root, "dan")
    # t.insert(t.root, "dada")
    # t.insert(t.root, "theire")

    # t = T.root
    # t.char = 't'
    #
    # hnode = TrieNode()
    # hnode.char = 'h'
    # t.children[charIndex('h')] = hnode
    #
    # enode = TrieNode()
    # enode.char = 'e'
    # hnode.children[charIndex('e')] = enode
    # enode.isEndOfWord = True
    #
    # rnode = TrieNode()
    # rnode.char = 'r'
    # enode.children[charIndex('r')] = rnode
    # rnode.isEndOfWord = True

    return t


def main():
    keys = ["the","the don",  "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in tire"]

    t = build_tree()
    traverse(t.root)

    # print t
    node = t.search(t.root, 'the')
    # print node.__dict__
    print get_closure_words('th', node)


def get_closure_words(pref, node):
    # import pdb;pdb.set_trace()
    if not node:
        return []
    word = pref + node.char
    if node.isEndOfWord:
        childs = filter(lambda x: x, node.children)
        v = [word]
        for o in childs:
            v.extend(get_closure_words(word, o))
        return v
    v=[]
    for o in filter(lambda x: x,node.children):
        v.extend(get_closure_words(word, o))
    return v

if __name__ == '__main__':
    main()
