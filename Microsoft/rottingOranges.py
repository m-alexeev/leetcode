from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    numOranges, minutes, N, M = 0, 0, len(grid), len(grid[0])
    frontier = deque([])
    for x, row in enumerate(grid):
        for y, orng in enumerate(row):
            if orng == 1:
                numOranges += 1
            if orng == 2:
                frontier.append((x, y))
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while frontier:
        for _ in range(len(frontier)):
            cur = frontier.popleft()
            for dir in dirs:
                r = cur[0] + dir[0]
                c = cur[1] + dir[1]
                if 0 <= r < N and 0 <= c < M and grid[r][c] == 1:
                    grid[r][c] = 2
                    frontier.append((r, c))
                    numOranges -= 1

        minutes += 1

    if minutes > 0:
        minutes -= 1
    return minutes if numOranges == 0 else -1


print(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
