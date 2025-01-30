from typing import List
from utils.helpers import printMatrix


def minPathSum(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])

    dp = [[0] * COLS for _ in range(ROWS)]
    # populate first row and col
    dp[0][0] = grid[0][0]
    for i in range(1, ROWS):
        dp[i][0] = grid[i][0] + dp[i - 1][0]
    for i in range(1, COLS):
        dp[0][i] = grid[0][i] + dp[0][i - 1]

    for row in range(1, ROWS):
        for col in range(1, COLS):
            dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]

    return dp[-1][-1]


print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(minPathSum([[1, 2, 3], [4, 5, 6]]))
