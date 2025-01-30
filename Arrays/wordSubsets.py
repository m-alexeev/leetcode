from typing import List


def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    maps = []
    for i, word in enumerate(words1):
        maps.append({})
        for l in word:
            maps[i][l] = maps[i].get(l, 0) + 1

    def counts(word):
        m = {}
        for i in word:
            m[i] = m.get(i, 0) + 1
        return m

    w2map = {}
    for w in words2:
        for l, c in counts(w).items():
            w2map[l] = max(w2map.get(l, c), c)

    res = []
    for i, w in enumerate(maps):
        print(w)
        print(w2map)
        add = True
        for l in w2map:
            if l not in w:
                add = False
            if l in w and w2map[l] > w[l]:
                add = False
        if add:
            res.append(words1[i])
    return res


print(
    wordSubsets(
        ["amazon", "apple", "facebook", "google", "leetcode"],
        ["e", "o"],
    )
)
