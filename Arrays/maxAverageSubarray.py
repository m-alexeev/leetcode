from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    avg = sum(nums[:k])
    l, r = 0, k
    cur = avg
    while r < len(nums):
        cur = cur + nums[r] - nums[l]
        r += 1
        l += 1
        avg = max(avg, cur)
    return avg / k


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage([5], 1))
print(findMaxAverage([0, 4, 0, 3, 2], 1))
