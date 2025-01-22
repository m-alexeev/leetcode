from typing import List


def search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        midpoint = (l + r) // 2
        if nums[midpoint] == target:
            return midpoint

        if nums[l] <= nums[midpoint]:
            if nums[l] <= target < nums[midpoint]:
                r = midpoint - 1
            else:
                l = midpoint + 1
        else:
            if nums[r] >= target > nums[midpoint]:
                l = midpoint + 1
            else:
                r = midpoint - 1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
