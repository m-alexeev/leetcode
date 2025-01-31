from typing import List


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    ROWS = len(matrix)
    if ROWS == 0:
        return 0
    COLS = len(matrix[0])

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    cache = {}

    def dfs(point):
        nonlocal cache
        if point in cache:
            return cache[point]
        maxPath = 1
        for dir in directions:
            nextRow, nextCol = (point[0] + dir[0], point[1] + dir[1])
            if (
                nextRow >= 0
                and nextRow < ROWS
                and nextCol >= 0
                and nextCol < COLS
                and matrix[nextRow][nextCol] > matrix[point[0]][point[1]]
            ):
                maxPath = max(maxPath, dfs((nextRow, nextCol)) + 1)
        cache[point] = maxPath
        return maxPath

    longestPath = 0
    for row in range(ROWS):
        for col in range(COLS):
            path = dfs((row, col))
            longestPath = max(path, longestPath)
    return longestPath


print(longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
print(longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
print(longestIncreasingPath([[7, 7, 5], [2, 4, 6], [8, 2, 0]]))
