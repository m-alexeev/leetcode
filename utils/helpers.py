from typing import List


def printMatrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        for col in row:
            print(col, end="\t")
        print("")
    print("")
