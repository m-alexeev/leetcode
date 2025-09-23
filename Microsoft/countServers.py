from typing import List


def countServers(grid: List[List[int]]) -> int:
    N, M = len(grid), len(grid[0])
    countCols = [0] * M
    countRows = [0] * N
    servers = 0
    for x in range(N):
        for y in range(M):
            if grid[x][y]:
                servers += 1
                countCols[y] += 1
                countRows[x] += 1
    for x in range(N):
        for y in range(M):
            if grid[x][y] and countCols[y] == 1 and countRows[x] == 1:
                servers -= 1
    return servers


print(countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
print(countServers([[1, 0], [1, 1]]))
print(countServers([[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]]))
