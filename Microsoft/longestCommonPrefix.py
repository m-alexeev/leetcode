from typing import List
from Trie import Trie, TrieNode


def longestCommonPrefix(strs: List[str]) -> str:
    # Create a trie from all the words
    trie = Trie()

    shortestWord = strs[0]
    for word in strs:
        if (len(word)) < len(shortestWord):
            shortestWord = word
        trie.insert(word)

    return trie.longestCommonPrefix(shortestWord)


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
