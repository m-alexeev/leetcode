from typing import List


def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    digit_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    res = []
    N = len(digits)

    def backtrack(s: str, start):
        nonlocal digit_map, res, N, digits
        if start == N:
            res.append(s)
            return
        for char in digit_map[digits[start]]:
            backtrack(s + char, start + 1)

    backtrack("", 0)
    return res


print(letterCombinations("23"))
