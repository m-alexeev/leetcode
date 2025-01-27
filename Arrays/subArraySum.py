from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    sums = 0
    running_sum = 0
    prefix_sum = {0: 1}
    for num in nums:
        running_sum += num
        if running_sum - k in prefix_sum:
            sums += prefix_sum[running_sum - k]
        prefix_sum[running_sum] = prefix_sum.get(running_sum, 0) + 1

    return sums


print(subarraySum([1, 1, 1], 2))
print(subarraySum([1, 2, 3], 3))
