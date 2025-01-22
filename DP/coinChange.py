import collections
from typing import List
from collections import deque


def coinChange(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0
    coins.sort(reverse=True)

    cache = {}
    min_level = 0
    q = deque([amount])
    while q:
        N = len(q)
        for _ in range(N):
            cur = q.popleft()
            if cur in cache:
                continue
            for i in coins:
                if cur in cache:
                    return cache[cur]
                if cur - i == 0:
                    return min_level + 1
                if cur > 0:
                    q.append(cur - i)
            cache[cur] = min_level
        min_level += 1
    return -1


print(coinChange([1, 2, 5], 11))
print(coinChange([2], 3))
print(coinChange([1], 3))
print(coinChange([1], 0))
