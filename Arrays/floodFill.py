from typing import List
from utils.helpers import printMatrix


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    ROWS = len(image)
    COLS = len(image[0])
    visited = set()
    colorToFill = image[sr][sc]
    if colorToFill == color:
        return image

    image[sr][sc] = color

    def dfs(row: int, col: int):
        if (row, col) in visited:
            return
        image[row][col] = color
        visited.add((row, col))

        if row - 1 >= 0 and image[row - 1][col] == colorToFill:
            dfs(row - 1, col)
        if row + 1 < ROWS and image[row + 1][col] == colorToFill:
            dfs(row + 1, col)
        if col - 1 >= 0 and image[row][col - 1] == colorToFill:
            dfs(row, col - 1)
        if col + 1 < COLS and image[row][col + 1] == colorToFill:
            dfs(row, col + 1)

    dfs(sr, sc)
    return image


printMatrix(floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
# printMatrix(floodFill([[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0))
