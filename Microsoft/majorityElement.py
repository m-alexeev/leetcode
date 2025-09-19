from typing import List


def majorityElement(nums: List[int]) -> int:
    nums = sorted(nums)
    return nums[len(nums) // 2]
