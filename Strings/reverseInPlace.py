from typing import List


def reverseString(s: List[str]) -> None:
    N = len(s)
    l, r = 0, N - 1
    while l <= r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    print(s)
    return


reverseString(["h", "e", "l", "l", "o"])
reverseString(["H", "a", "n", "n", "a", "h"])
reverseString([])
reverseString(["A"])
