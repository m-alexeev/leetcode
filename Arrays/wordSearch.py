from typing import List


def exists(board: List[List[str]], word: str) -> bool:

    ROWS = len(board)
    COLS = len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(row, col, prefix, visited):
        nonlocal directions
        if prefix == len(word):
            return 1

        visited.add((row, col))
        maxLen = 0
        for dir in directions:
            nextRow, nextCol = row + dir[0], col + dir[1]
            if (
                0 <= nextRow < ROWS
                and 0 <= nextCol < COLS
                and board[nextRow][nextCol] == word[prefix]
                and (nextRow, nextCol) not in visited
            ):
                visited.add((nextRow, nextCol))
                maxLen = max(1 + dfs(nextRow, nextCol, prefix + 1, visited), maxLen)
        visited.remove((row, col))
        return maxLen

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == word[0]:
                matchLen = dfs(row, col, 1, set())
                print(matchLen)
                if matchLen == len(word):
                    return True
    return False


print(exists([["a", "a"]], "aaa"))
print(
    exists(
        [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"
    )
)
# print(
#     exists(
#         board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
#         word="ABCCED",
#     )
# )
# print(
#     exists(
#         board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
#         word="SEE",
#     )
# )
# print(
#     exists(
#         board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
#         word="ABCB",
#     )
# )
