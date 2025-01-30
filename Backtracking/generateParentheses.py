from typing import List


def generateParenthesis(n: int) -> List[str]:
    res = []

    def backtrack(cur, open: int, close: int):
        if open == 0 == close:
            res.append(cur)
        else:
            if open > 0:
                backtrack(cur + "(", open - 1, close)
            if close > 0 and close > open:
                backtrack(cur + ")", open, close - 1)

    backtrack("", n, n)
    return res


print(generateParenthesis(3))
