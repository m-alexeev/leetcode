from typing import List


def houseRobber(nums: List[int]) -> int:
    N = len(nums)
    if N == 0:
        return 0
    if N == 1:
        return nums[0]
    if N == 2:
        return max(nums[0], nums[1])
    dp = [0] * N
    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2, N):
        dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
    print(dp)
    return max(dp[-1], dp[-2])


print(houseRobber([1, 2, 3, 1]))
print(houseRobber([5, 2, 3, 2, 6]))
print(houseRobber([5, 2, 3, 6]))
print(houseRobber([1, 1]))
print(houseRobber([1, 3, 1]))
