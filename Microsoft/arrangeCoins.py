from math import sqrt


def arrangeCoins(n: int) -> int:
    return int((sqrt(8 * n + 1) - 1) // 2)


print(arrangeCoins(5))
print(arrangeCoins(8))
