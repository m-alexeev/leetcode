from types import MappingProxyType
from typing import List


def maxConsecutiveOnes(nums: List[int], k: int) -> int:
    l = r = mx = zeros = 0
    N = len(nums)
    while r < N:
        if nums[r] == 1:
            r += 1
        else:
            if zeros == k:
                while zeros == k:
                    if nums[l] == 0:
                        zeros -= 1
                    l += 1
            else:
                r += 1
                zeros += 1
        mx = max(mx, r - l)
    return mx


nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
print(maxConsecutiveOnes(nums, 3))
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
print(maxConsecutiveOnes(nums, 2))
