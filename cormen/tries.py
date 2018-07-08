class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_eow = False
        self.counter = 0


class Trie(object):
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    @staticmethod
    def _char_to_index(c):
        return ord(c) - ord('a')

    def insert(self, key):
        current = self.root
        length = len(key)

        for level in range(length):
            index = Trie._char_to_index(key[level])
            if not current.children.get(index):
                current.children[index] = self.get_node()
            current = current.children[index]
            current.counter += 1
        current.is_eow = True

    def search(self, key):
        current = self.root
        length = len(key)

        for level in range(length):
            index = self._char_to_index(key[level])
            if not current.children.get(index):
                return False
            current = current.children[index]

        return current is not None and current.is_eow

    def count_prefix(self, key):
        current = self.root
        length = len(key)

        for level in range(length):
            index = self._char_to_index(key[level])
            if current.children.get(index) is None:
                return 0
            current = current.children[index]

        return current.counter

    def count_children(self, node):
        if node is None:
            return 0
        else:
            ztack = []
            ztack.append(node)
            s = 0
            while ztack:
                e = ztack.pop()
                if e.is_eow:
                    s += 1
                for k in e.children:
                    if k is not None:
                        ztack.append(k)
            return s


if __name__ == '__main__':
    keys = ["hack", "hacker", "hay"]
    t = Trie()
    for k in keys:
        t.insert(k)

    w = "hay"
    print("Word: %s in trie: %s" % (w, t.search(w)))
    w = "hac"
    print("Prefix: %s in trie count: %s" % (w, t.count_prefix(w)))
