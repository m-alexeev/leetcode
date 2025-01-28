from typing import List
from utils.helpers import printMatrix


def numDistinctIslands(grid: List[List[int]]) -> int:
    islands = set()
    visited = set()
    cur_island = []
    ROWS = len(grid)
    COLS = len(grid[0])

    def dfs(abs, rel):
        nonlocal cur_island, grid
        row, col = abs
        visited.add(abs)
        cur_island.append(rel)
        if row > 0 and grid[row - 1][col] == 1 and (row - 1, col) not in visited:
            dfs((row - 1, col), (rel[0] - 1, rel[1]))
        if row < ROWS - 1 and grid[row + 1][col] == 1 and (row + 1, col) not in visited:
            dfs((row + 1, col), (rel[0] + 1, rel[1]))
        if col > 0 and grid[row][col - 1] == 1 and (row, col - 1) not in visited:
            dfs((row, col - 1), (rel[0], rel[1] - 1))
        if col < COLS - 1 and grid[row][col + 1] == 1 and (row, col + 1) not in visited:
            dfs((row, col + 1), (rel[0], rel[1] + 1))

    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) not in visited and grid[i][j] == 1:
                cur_island = []
                dfs((i, j), (0, 0))
                islands.add(tuple(cur_island))
    print(islands)
    return len(islands)


print(
    numDistinctIslands(
        [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    )
)
print(
    numDistinctIslands(
        [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    )
)
