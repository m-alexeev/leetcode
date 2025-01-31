def wordBreak(s: str, wordDict) -> bool:
    N = len(s)
    maxLen = max([len(w) for w in wordDict])
    dp = [False] * (N + 1)
    dp[0] = True
    for i in range(1, N + 1):
        for j in range(i - 1, i - maxLen - 1, -1):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[N]


print(wordBreak("leetcode", ["leet", "code"]))
# print(wordBreak("applepenapple", wordDict=["apple", "pen"]))
# print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
# print(wordBreak(s="abcd", wordDict=["a", "abc", "b", "cd"]))

# cat, cats, sand, and, dog
