from collections import deque
from typing import List
from utils.helpers import printMatrix


def wallsAndGates(rooms: List[List[int]]) -> None:
    rows = len(rooms)
    cols = len(rooms[0])
    # find all gates
    q = deque()
    for i in range(rows):
        for j in range(cols):
            if rooms[i][j] == 0:
                q.append((i, j))
    distance = 1
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            # add neighbors to queue
            for dir in directions:
                neighbor = (cur[0] + dir[0], cur[1] + dir[1])
                if (
                    neighbor[0] >= 0
                    and neighbor[0] < rows
                    and neighbor[1] >= 0
                    and neighbor[1] < cols
                    and rooms[neighbor[0]][neighbor[1]] != -1
                    and rooms[neighbor[0]][neighbor[1]] > distance
                ):
                    rooms[neighbor[0]][neighbor[1]] = distance
                    q.append(neighbor)
        distance += 1
    printMatrix(rooms)
    return


print(
    wallsAndGates(
        [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
    )
)
