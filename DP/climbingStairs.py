def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [1, 2]
    for i in range(2, n):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[-1]


print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(6))
