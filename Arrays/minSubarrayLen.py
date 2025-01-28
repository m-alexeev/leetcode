from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    N = len(nums)
    if N == 0:
        return N
    l = 0
    minLen = 10**5 + 1
    r = 0
    cur = 0
    for r in range(N):
        cur += nums[r]
        r += 1
        while cur >= target:
            minLen = min(minLen, r - l)
            cur -= nums[l]
            l += 1

    return 0 if minLen == 10**5 else minLen


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(4, [1, 4, 4]))
print(minSubArrayLen(11, [1, 4, 4]))
print(minSubArrayLen(6, [10, 2, 3]))
