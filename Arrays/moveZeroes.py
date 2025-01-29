from typing import List


def moveZeros(nums: List[int]) -> None:
    zeros = 0
    N = len(nums)
    for i in range(N):
        if nums[i] == 0:
            zeros += 1
        else:
            nums[i - zeros] = nums[i]

    for i in range(zeros):
        nums[N - i - 1] = 0

    print(nums)


print(moveZeros([0, 1, 0, 3, 12]))
print(moveZeros([0]))
