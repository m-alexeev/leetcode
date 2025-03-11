from typing import List


def buyAndSellStock(prices: List[int]) -> int:
    N = len(prices)
    profit = 0
    l, r = 0, 1
    while r < N:
        if prices[r] > prices[l]:
            profit = max(profit, prices[r] - prices[l])
        else:
            l = r
        r += 1

    return profit


print(buyAndSellStock([7, 1, 5, 3, 6, 4]))
print(buyAndSellStock([7, 4, 3]))


def buyAndSellStockII(prices: List[int]) -> int:
    if not prices:
        return 0
    profit = 0
    l = r = 0
    N = len(prices)

    while r < N - 1:
        if prices[r] < prices[r + 1]:
            r += 1
            if r == N - 1:
                # sell on last day
                profit += prices[r] - prices[l]
        else:
            profit += prices[r] - prices[l]
            r += 1
            l = r
    return profit


# print(buyAndSellStockII([7, 1, 5, 3, 6, 4]))
# print(buyAndSellStockII([1, 2, 3, 4, 5]))
