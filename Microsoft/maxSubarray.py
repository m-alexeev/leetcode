from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    maxAvg = sum(nums[:k]) / k
    cur = sum(nums[:k])
    l = 0
    for r in range(k, len(nums)):
        cur -= nums[l]
        cur += nums[r]
        maxAvg = max(cur / k, maxAvg)
        l += 1

    return maxAvg


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage([5], 1))
