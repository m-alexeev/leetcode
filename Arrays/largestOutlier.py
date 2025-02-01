from typing import List
from collections import Counter


def getLargestOutlier(nums: List[int]) -> int:
    total = sum(nums)
    d = Counter(nums)
    outlier = -(10**10)

    for num in nums:
        d[num] -= 1
        total -= num
        if total % 2 == 0 and d[total // 2] > 0:
            outlier = max(outlier, num)

        d[num] += 1
        total += num
    return outlier


print(getLargestOutlier([2, 3, 5, 10]))
