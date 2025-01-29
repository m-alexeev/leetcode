from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    N = len(nums)
    out = [1] * N

    # prefixes
    prefix = 1
    for i in range(N):
        out[i] = prefix
        prefix *= nums[i]

    # postfixes
    postfix = 1
    for i in range(N - 1, -1, -1):
        out[i] *= postfix
        postfix *= nums[i]
    return out


print(productExceptSelf([1, 2, 3, 4]))
