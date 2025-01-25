from collections import deque
from typing import List


def rottingOranges(grid: List[List]) -> int:
    q = deque()
    ROWS = len(grid)
    COLS = len(grid[0])
    orangesLeft = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 2:
                q.append((row, col))
            elif grid[row][col] == 1:
                orangesLeft += 1
    steps = 0
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            r, c = cur
            for dir in dirs:
                row = r + dir[0]
                col = c + dir[1]
                if (0 <= row < ROWS) and (0 <= col < COLS) and grid[row][col] == 1:
                    q.append((row, col))
                    orangesLeft -= 1
                    grid[row][col] = 2
        steps += 1
    if steps > 0:
        steps -= 1
    return steps if orangesLeft == 0 else -1


print(rottingOranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(rottingOranges([[0]]))
