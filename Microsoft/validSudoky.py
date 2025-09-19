from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    cols = [set() for _ in range(9)]
    rows = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for x, row in enumerate(board):
        for y, val in enumerate(row):
            if val == ".":
                continue
            if val in cols[y]:
                return False
            else:
                cols[y].add(val)
            if val in rows[x]:
                return False
            else:
                rows[x].add(val)
            boxIndex = x // 3 + ((y // 3) * 3)
            if val in boxes[boxIndex]:
                return False
            else:
                boxes[boxIndex].add(val)
    return True


print(
    isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
