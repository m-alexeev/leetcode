from typing import List
from math import ceil


def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)

    def findHours(k):
        nonlocal piles
        hours = 0
        for i in piles:
            hours += int(ceil(i / k))
        return hours

    while l <= r:
        midpoint = l + (r - l) // 2
        hours = findHours(midpoint)
        # print(midpoint, hours)
        if hours > h:
            l = midpoint + 1
        else:
            r = midpoint - 1

    return l


print(minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
