from typing import List
from utils.helpers import printMatrix


def rotate(matrix: List[List[int]]) -> None:
    def swap(one, two):
        temp = matrix[one[0]][one[1]]
        matrix[one[0]][one[1]] = matrix[two[0]][two[1]]
        matrix[two[0]][two[1]] = temp

    # swap rows
    N = len(matrix)
    for i in range(N // 2):
        for j in range(N):
            swap([i, j], [N - 1 - i, j])

    # rotate
    for col in range(N):
        for row in range(col, N):
            print((row, col))
            swap([row, col], [col, row])
    printMatrix(matrix)
    return


rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
