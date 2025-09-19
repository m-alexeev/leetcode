class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.numChildren = 0
        self.isWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, key):
        curr: TrieNode = self.root
        for c in key:
            index = ord(c.lower()) - ord("a")
            if curr.children[index] is None:
                new_node: TrieNode = TrieNode()
                curr.children[index] = new_node
                curr.numChildren += 1
            curr = curr.children[index]
        curr.isWord = True

    def search(self, word) -> bool:
        curr = self.root
        for c in word:
            index = ord(c.lower()) - ord("a")
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isWord

    def longestCommonPrefix(self, word) -> str:
        prefix = ""
        cur = self.root
        for c in word:
            if cur.numChildren > 1:
                return prefix
            prefix += c
            index = ord(c.lower()) - ord("a")
            cur = cur.children[index]
        return prefix

    def isPrefix(self, word) -> bool:
        cur = self.root
        for c in word:
            index = ord(c.lower()) - ord("a")
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
        return True


if __name__ == "__main__":
    trie = Trie()

    arr = ["and", "ant", "do", "dad"]
    for s in arr:
        trie.insert(s)
    searchKeys = ["do", "gee", "bat"]
    for s in searchKeys:
        if trie.search(s):
            print("true", end=" ")
        else:
            print("false", end=" ")

    print()
    prefixKeys = ["ge", "ba", "do", "de"]
    for s in prefixKeys:
        if trie.isPrefix(s):
            print("true", end=" ")
        else:
            print("false", end=" ")
    print()
