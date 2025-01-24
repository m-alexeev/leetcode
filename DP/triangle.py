from typing import List

from utils.helpers import printMatrix


def minimalTotal(triangle: List[List[int]]) -> int:
    N = len(triangle)
    dp = [[0] * N for _ in range(N)]
    # set up bottom row
    for i in range(N):
        dp[N - 1][i] = triangle[N - 1][i]

    for i in range(N - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
    printMatrix(dp)
    return dp[0][0]


print(minimalTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(minimalTotal([[-11]]))
