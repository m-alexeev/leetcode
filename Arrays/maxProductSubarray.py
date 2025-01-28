from typing import List


def maxProduct(nums: List[int]) -> int:
    mx = -(10**10)
    prod = 1
    for i in nums:
        prod *= i
        mx = max(prod, mx)
        if prod == 0:
            prod = 1
    prod = 1
    for i in nums[::-1]:
        prod *= i
        mx = max(prod, mx)
        if prod == 0:
            prod = 1
    return mx


print(maxProduct([2, 3, -2, 4]))
