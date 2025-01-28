class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insertWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.word

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True
