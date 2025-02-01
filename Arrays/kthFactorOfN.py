from collections import deque
from math import sqrt
from typing import List


def kthFactor(n: int, k: int) -> int:
    # naive o(n)
    # factors = 0
    # for i in range(1, n + 1):
    #     if n % i == 0:
    #         factors += 1
    #         if factors == k:
    #             return i
    # sqrt
    f1 = []
    f2 = deque()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            f1.append(i)
            f2.appendleft(n // i)
    if f1[-1] == f2[0]:
        f2.popleft()
    f1 += list(f2)
    return f1[k - 1] if k <= len(f1) else -1


print(kthFactor(12, 3))
print(kthFactor(7, 2))
print(kthFactor(4, 4))
