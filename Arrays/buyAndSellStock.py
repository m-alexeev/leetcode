from typing import List


def buyAndSellStockII(nums: List[int]) -> int:
    if not nums:
        return 0
    profit = 0
    l = r = 0
    N = len(nums)

    while r < N - 1:
        if nums[r] < nums[r + 1]:
            r += 1
            if r == N - 1:
                # sell on last day
                profit += nums[r] - nums[l]
        else:
            profit += nums[r] - nums[l]
            r += 1
            l = r
    return profit


print(buyAndSellStockII([7, 1, 5, 3, 6, 4]))
print(buyAndSellStockII([1, 2, 3, 4, 5]))
