from typing import List


def twoSum(nums: List[int], i: int, res: List[List[int]]) -> None:
    seen = set()
    j = i + 1
    while j < len(nums):
        complement = -nums[i] - nums[j]
        if complement in seen:
            res.append([nums[i], nums[j], complement])
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
        seen.add(nums[j])
        j += 1


def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSum(nums, i, res)
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 0, 0]))
print(threeSum([0, 0, 0, 0]))
