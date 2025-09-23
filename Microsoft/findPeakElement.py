from typing import List
from math import inf


def findPeakElement(nums: List[int]) -> int:
    N = len(nums)
    l, r = 0, N - 1
    if N <= 1:
        return 0
    while l <= r:
        mid = l + ((r - l) // 2)
        left, right = -inf, -inf
        if mid > 0:
            left = nums[mid - 1]
        if mid < N - 1:
            right = nums[mid + 1]

        if left < nums[mid] > right:
            return mid
        if nums[mid] < right:
            l = mid + 1
        else:
            r = mid - 1

    return -1


print(findPeakElement([1, 2, 3, 4]))
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
