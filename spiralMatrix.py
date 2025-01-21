from typing import List


def spiralMatrix(matrix: List[List[int]]) -> List[int]:
    res = []
    N = len(matrix)
    M = len(matrix[0])
    left, right, top, bottom = 0, M - 1, 0, N - 1
    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            res.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            res.append(matrix[row][right])
        right -= 1
        for col in range(right, left - 1, -1):
            res.append(matrix[bottom][col])
        bottom -= 1
        for row in range(bottom, top - 1, -1):
            res.append(matrix[row][left])
        left += 1
    return res[: M * N]


print(spiralMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
