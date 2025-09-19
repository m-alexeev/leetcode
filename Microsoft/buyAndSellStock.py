from typing import List


def buyAndSellStock(prices: List[int]) -> int:

    profit = 0
    N, l, r = len(prices), 0, 1
    while r < N:
        if prices[r] > prices[l]:
            profit = max(profit, prices[r] - prices[l])
        else:
            l = r
        r += 1

    return profit


print(buyAndSellStock([7, 1, 5, 3, 6, 4]))
print(buyAndSellStock([7, 6, 4, 3, 1]))
print(buyAndSellStock([1, 5, 0, 6]))
