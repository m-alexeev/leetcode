from typing import List
from utils.Trie import Trie


def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    res = []
    trie = Trie()

    products.sort()
    for product in products:
        trie.insertWord(product)

    prefix = ""
    for c in searchWord:
        prefix += c
        suggestions = []
        collectWords(trie, prefix, suggestions)
        res.append(suggestions)

    return res


def collectWords(trie, prefix, suggestions):
    def dfs(node, path):
        if len(suggestions) == 3:
            return
        if node.word:
            suggestions.append(path)
        for char in sorted(node.children):
            dfs(node.children[char], path + char)

    cur = trie.root
    for c in prefix:
        if c not in cur.children:
            return
        cur = cur.children[c]

    dfs(cur, prefix)


print(
    suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
)
