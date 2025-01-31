from heapq import heapify, heappop
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    groups = {}
    for i in nums:
        groups[i] = groups.get(i, 0) + 1
    heap = []
    for item, count in groups.items():
        heap.append((-count, item))

    res = []
    heapify(heap)
    print(heap)
    while k > 0:
        res.append(heappop(heap)[1])
        k -= 1
    return res


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
print(topKFrequent([1], 1))
print(topKFrequent([5, 2, 5, 3, 5, 3, 1, 1, 3], 2))
