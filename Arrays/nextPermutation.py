from typing import List


def nextPermuration(nums: List[int]) -> None:
    # find first decreasing element from the right side
    N = len(nums)
    first_decreasing = None
    for i in range(N - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            first_decreasing = i - 1
            break

    print(first_decreasing)

    if first_decreasing is None:
        nums.reverse()
        return

    # Find smallest element in right side such that its greater
    # than first decreasing
    smallest = first_decreasing + 1
    for i in range(N - 1, first_decreasing, -1):
        if nums[i] > nums[first_decreasing]:
            smallest = i
            break

    # swap first_decreasing and smallest
    nums[first_decreasing], nums[smallest] = nums[smallest], nums[first_decreasing]
    # swap first_decreasing with smallest and reverse
    nums[first_decreasing + 1 :] = reversed(nums[first_decreasing + 1 :])

    print(nums)


nextPermuration([1, 2, 3])  # 1,3,2
nextPermuration([3, 2, 1])  # 1,2,3
nextPermuration([4, 3, 2, 1])  # 1,2,3
nextPermuration([1, 1, 5])  # 1,5,1
nextPermuration([1, 3, 2])  # 1,5,1
