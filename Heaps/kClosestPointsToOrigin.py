import enum
from heapq import heapify, heappop
from typing import List
from math import sqrt


def kClosest(points: List[[List[int]]], k: int) -> List[List[int]]:
    res = []

    heap = []
    for i, (x, y) in enumerate(points):
        heap.append((sqrt(x * x + y * y), i))
    heapify(heap)

    for _ in range(k):
        _, point = heappop(heap)
        res.append(points[point])
    return res


print(kClosest([[1, 3], [-2, 2]], 1))
print(kClosest([[3, 3], [5, -1], [-2, 4]], 2))
