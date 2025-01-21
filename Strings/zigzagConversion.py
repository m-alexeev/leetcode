def printMatrix(matrix):
    for row in matrix:
        print(row)


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    # Find num cols
    N = len(s)
    letters = 0
    cols = 0
    while letters < N:
        if numRows <= 2 or cols % (numRows - 1) == 0:
            letters += numRows
        else:
            letters += 1
        cols += 1
    matrix = [[""] * cols for _ in range(numRows)]

    N = len(matrix)
    row = col = 0
    dir = 1
    for let in s:
        matrix[row][col] = let
        if dir == 1 and row < N - 1:
            row += 1
        else:
            row -= 1
            col += 1
        if row == N - 1:
            dir = 0
        if row == 0:
            dir = 1

    # printMatrix(matrix)
    res = ""
    for row in matrix:
        res += "".join(row)
    return res


print(convert("PAYPALISHIRING", 1))
print(convert("PAYPALISHIRING", 2))
print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
