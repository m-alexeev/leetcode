from typing import List


def maxSubarray(nums: List[int]) -> int:
    l, r, s, N = 0, 0, 0, len(nums)
    if N == 0:
        return 0
    if N == 1:
        return nums[0]
    rs = 0
    while r < N:
        if rs + nums[r] > 0:
            rs += nums[r]
        else:
            s = max(s, rs)

    return s
