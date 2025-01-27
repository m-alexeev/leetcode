from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    found = set()
    res = set()
    N = len(s)
    if N <= 10:
        return list(res)

    for i in range(0, N - 9):
        cur = s[i : i + 10]
        if cur in found:
            res.add(cur)
        else:
            found.add(cur)
        print(cur)
    return list(res)


print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))
print(findRepeatedDnaSequences("AAAAAAAAAAA"))
