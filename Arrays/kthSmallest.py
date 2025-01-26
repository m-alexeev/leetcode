from typing import List
from heapq import heapify, heappush, heappop


def kthSmallestMatrix(matrix: List[List[int]], k: int) -> int:
    ROWS = len(matrix)
    COLS = len(matrix[0])
    heap = []
    heappush(heap, (matrix[0][0], 0, 0))
    visited = set((0, 0))
    for i in range(k - 1):
        val, r, c = heappop(heap)
        if c < COLS - 1:
            if (r, c + 1) not in visited:
                heappush(heap, (matrix[r][c + 1], r, c + 1))
                visited.add((r, c + 1))
        if r < ROWS - 1:
            if (r + 1, c) not in visited:
                heappush(heap, (matrix[r + 1][c], r + 1, c))
                visited.add((r + 1, c))
        print(i, heap)
    return heappop(heap)[0]


print(kthSmallestMatrix([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 7))
print(kthSmallestMatrix([[1, 2], [1, 3]], 2))
print(kthSmallestMatrix([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 6))
print(kthSmallestMatrix([[-5]], 1))
