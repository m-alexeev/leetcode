from typing import List


def uniquePathsWithoutObstacles(obstacleGrid: List[List[int]]) -> int:
    ROWS = len(obstacleGrid)
    COLS = len(obstacleGrid[0])
    dp = [[0] * COLS for _ in range(ROWS)]

    # Setup DP matrix
    for i in range(ROWS):
        if obstacleGrid[i][0] == 1:
            break
        else:
            dp[i][0] = 1
    for i in range(COLS):
        if obstacleGrid[0][i] == 1:
            break
        else:
            dp[0][i] = 1

    for row in range(1, ROWS):
        for col in range(1, COLS):
            if obstacleGrid[row][col] == 0:
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    return dp[-1][-1]


print(uniquePathsWithoutObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(uniquePathsWithoutObstacles([[0, 1], [0, 0]]))
