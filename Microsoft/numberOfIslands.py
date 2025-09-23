from typing import List


def numberOfIslands(grid: List[List[str]]) -> int:
    islands = 0
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(x, y):
        nonlocal grid
        grid[x][y] = "-1"
        if x > 0 and grid[x - 1][y] == "1":
            dfs(x - 1, y)
        if x < ROWS - 1 and grid[x + 1][y] == "1":
            dfs(x + 1, y)
        if y > 0 and grid[x][y - 1] == "1":
            dfs(x, y - 1)
        if y < COLS - 1 and grid[x][y + 1] == "1":
            dfs(x, y + 1)

    for x in range(ROWS):
        for y in range(COLS):
            if grid[x][y] == "1":
                islands += 1
                dfs(x, y)

    return islands


print(
    numberOfIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
