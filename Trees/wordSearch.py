from typing import List
from utils.Trie import Trie, TrieNode


def wordSearchII(board: List[List[str]], words: List[str]) -> List[str]:
    # Create trie
    trie = Trie()
    for word in words:
        trie.insertWord(word)
    ROWS = len(board)
    COLS = len(board[0])

    foundWords = set()
    visited = set()

    # Search for words
    def dfs(prefix, row, col):
        nonlocal board, visited
        print(prefix, visited)
        visited.add((row, col))
        if trie.startsWith(prefix):
            if row > 0 and (row - 1, col) not in visited:
                dfs(prefix + board[row - 1][col], row - 1, col)
            if row < ROWS - 1 and (row + 1, col) not in visited:
                dfs(prefix + board[row + 1][col], row + 1, col)
            if col > 0 and (row, col - 1) not in visited:
                dfs(prefix + board[row][col - 1], row, col - 1)
            if col < COLS - 1 and (row, col + 1) not in visited:
                dfs(prefix + board[row][col + 1], row, col + 1)
        if trie.search(prefix):
            foundWords.add(prefix)
        visited.remove((row, col))

    for row in range(ROWS):
        for col in range(COLS):
            visited = set()
            dfs(board[row][col], row, col)

    return list(foundWords)


print(
    wordSearchII(
        board=[
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        words=["oath", "pea", "eat", "rain"],
    )
)

print(
    wordSearchII(
        [["a", "b", "c", "e"], ["x", "x", "c", "d"], ["x", "x", "b", "a"]],
        ["abc", "abcd"],
    )
)
