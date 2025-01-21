from typing import List


def longestIncreasingSubsequence(nums: List[int]) -> int:
    N = len(nums)
    dp = [1] * N
    i = N - 2
    while i >= 0:
        j = i + 1
        while j < N:
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
            j += 1
        i -= 1
    return max(dp)


print(longestIncreasingSubsequence([1, 3, 2, 5, 6]))
print(longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]))
