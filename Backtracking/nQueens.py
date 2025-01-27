from typing import List
from utils.helpers import printMatrix


def solveNQueens(n: int) -> List[List[str]]:

    def backtrack(r):
        if r == n:
            new = []
            for i in board:
                new.append("".join(i))
            res.append(new)
            return
        for c in range(n):
            if c not in cols and r + c not in diag_pos and r - c not in diag_neg:
                board[r][c] = "Q"
                cols.add(c)
                diag_pos.add(r + c)
                diag_neg.add(r - c)

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                diag_pos.remove(r + c)
                diag_neg.remove(r - c)

    cols = set()
    diag_pos = set()
    diag_neg = set()
    board = [["."] * n for _ in range(n)]
    res = []
    backtrack(0)
    return res


print(solveNQueens(4))
