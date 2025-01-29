from typing import List
from heapq import heappop, heappush, heapify


def minimumOperations(nums: List[int]) -> int:
    ops = 0
    heap = list(set(nums))

    heapify(heap)

    # remove 0
    if heap[0] == 0:
        heappop(heap)

    prev = None
    while heap:
        cur = heappop(heap)
        if prev is None:
            prev = cur
        else:
            prev = cur + prev
        ops += 1

    return ops


print(minimumOperations([1, 5, 0, 3, 5]))
print(minimumOperations([0]))
