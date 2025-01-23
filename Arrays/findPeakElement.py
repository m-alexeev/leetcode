from typing import List


def findPeak(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        # print(mid)
        if mid == 0:
            if nums[mid] > nums[mid + 1]:
                return mid
            else:
                return mid + 1
        if mid == len(nums) - 1:
            if nums[mid] > nums[mid - 1]:
                return mid
            else:
                return mid - 1
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


print(findPeak([1, 2, 3, 1]))
print(findPeak([1, 2, 1, 3, 5, 6, 4]))
print(findPeak([0, 1]))
print(findPeak([3, 1, 2]))
