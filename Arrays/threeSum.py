from typing import List


def threeSum(nums: List[int]):
    N = len(nums)
    sums = set()
    nums.sort()
    for i in range(N - 2):
        cur = nums[i]
        l = i + 1
        r = N - 1
        while l < r:
            three_sum = cur + nums[l] + nums[r]
            if three_sum == 0:
                sums.add((cur, nums[l], nums[r]))
                l += 1
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                r -= 1
    return list(list(x) for x in sums)


# -1, 0, 1, 2, -1, -4
# -4 -1 -1  0   1   2
#
print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 1, 1]))
print(threeSum([0, 0, 0]))
