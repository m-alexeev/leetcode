from typing import List


def shiftingLetters(s: str, shifts: List[List[int]]) -> str:
    arr = [ord(c) - 97 for c in s]
    N = len(arr)
    moves = [0] * (N + 1)

    # Create shifts array
    for i in shifts:
        start, end, shift = i
        shift = 1 if shift == 1 else -1
        moves[start] += -shift
        moves[end + 1] += shift

    # shift letters
    prefix = moves[-1]
    for i in range(len(arr) - 1, -1, -1):
        arr[i] = (prefix + arr[i] + 26) % 26
        prefix += moves[i]
    print(arr)

    return "".join([chr(i + 97) for i in arr])


print(shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]))
print(shiftingLetters("dztz", [[0, 0, 0], [1, 1, 1]]))
