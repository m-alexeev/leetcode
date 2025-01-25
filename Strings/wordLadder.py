import collections
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    # Create adjacency list
    wordList.append(beginWord)
    adjacencies = collections.defaultdict(list)
    for word in wordList:
        for letter in range(len(word)):
            pattern = word[:letter] + "*" + word[letter + 1 :]
            adjacencies[pattern].append(word)

    visit = set([beginWord])
    q = collections.deque([beginWord])
    res = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            for l in range(len(cur)):
                p = cur[:l] + "*" + cur[l + 1 :]
                if p in adjacencies:
                    for w in adjacencies[p]:
                        if w not in visit:
                            q.append(w)
                            visit.add(w)
                        if endWord in visit:
                            return res + 2
        res += 1

    return 0


print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(ladderLength("hot", "dot", ["hot", "dot", "dog"]))
print(ladderLength("hot", "dog", ["hot", "dog"]))
