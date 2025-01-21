def numDecodings(s: str) -> int:
    N = len(s)
    if N == 0 or s[0] == "0":
        return 0

    dp = [0] * N
    dp[0] = 1

    for i in range(1, N):
        if s[i] != "0":
            dp[i] = dp[i - 1]

        if s[i - 1] != "0" and 10 <= int(s[i - 1] + s[i]) <= 26:
            dp[i] += dp[i - 2] if i >= 2 else 1
    return dp[N - 1]


print(numDecodings("12"))
print(numDecodings("11106"))
print(numDecodings("06"))
