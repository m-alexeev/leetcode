from re import L
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    pos = [-1, -1]
    N = len(nums)

    if N == 0:
        return pos

    l, r = 0, N - 1
    while l <= r:
        midpoint = l + (r - l) // 2
        if nums[midpoint] < target:
            l = l + 1
        else:
            r = r - 1
    if l < 0 or l >= N:
        return pos
    else:
        pos[0] = l

    print(l)
    r = N - 1
    while l <= r:
        midpoint = l + (r - l) // 2
        if nums[midpoint] <= target:
            l = l + 1
        else:
            r = r - 1

    pos[1] = l - 1
    return pos


print(searchRange([5, 7, 7, 7, 7, 8, 8, 10], 7))
print(searchRange([5, 7, 7, 8, 8, 8, 8, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 12))
