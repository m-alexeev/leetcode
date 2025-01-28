from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    N = len(nums)
    res = 1
    neg = 0
