from heapq import heappop, heappush
from typing import List
import random


def findKthLargest(nums: List[int], k: int) -> int:
    heap = []
    for i in nums:
        heappush(heap, -i)
    res = 0
    for i in range(k):
        res = heappop(heap)
    return -1 * res


def findKthLargestQuickSelect(nums: List[int], k: int) -> int:
    k = len(nums) - k + 1

    def quickSelect(arr, k):
        pivot = random.choice(arr)
        left = []
        right = []
        mid = []

        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])

        if k <= len(left):
            return quickSelect(left, k)
        if k > len(left) + len(mid):
            return quickSelect(right, k - len(left) - len(mid))
        return pivot

    return quickSelect(nums, k)


print(findKthLargestQuickSelect([3, 2, 1, 5, 6, 4], 2))
print(findKthLargestQuickSelect(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
