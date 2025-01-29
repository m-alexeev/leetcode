from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    # replace nums
    N = len(nums)
    for i in range(N):
        while nums[i] > 0 and nums[i] <= N and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(N):
        if nums[i] != i + 1:
            return i + 1
    return N + 1


print(firstMissingPositive([1, 2, 0]))
print(firstMissingPositive([3, 4, -1, 1]))
print(firstMissingPositive([7, 8, 9, 11, 12]))
