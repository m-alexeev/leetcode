from typing import List


def numIslands(grid: List[List[str]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])

    visited = set()

    def traverseIsland(row, col):
        nonlocal visited
        visited.add((row, col))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dir in directions:
            nextRow, nextCol = row + dir[0], col + dir[1]
            if (
                0 <= nextRow < ROWS
                and 0 <= nextCol < COLS
                and (nextRow, nextCol) not in visited
                and grid[nextRow][nextCol] == "1"
            ):
                traverseIsland(nextRow, nextCol)

    islands = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "1" and (row, col) not in visited:
                traverseIsland(row, col)
                islands += 1
    return islands


print(
    numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
print(
    numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
