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


def threeSumClosest(nums: List[int], target: int) -> int:
    N = len(nums)
    nums.sort()
    closest = abs(target - sum(nums[:3]))
    res = sum(nums[:3])
    for i in range(N - 2):
        l = i + 1
        r = N - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == target:
                return total
            if abs(target - total) < abs(closest):
                closest = abs(target - total)
                res = total
            if total < target:
                l += 1
            else:
                r -= 1

    return res


print(threeSumClosest([-1, 2, 1, -4], 1))
print(threeSumClosest([0, 0, 0], 1))
print(threeSumClosest([1, 1, 1, 0], 100))
print(threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))
