from typing import List


def wordBreak(s: str, wordDict) -> bool:
    wordDict = set(wordDict)
    N = len(s)
    dp = [False] * (N + 1)
    dp[N] = True
    for i in range(N - 1, -1, -1):
        for w in wordDict:
            if i + len(w) <= N and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]

    return dp[0]


print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("applepenapple", wordDict=["apple", "pen"]))
print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
print(wordBreak(s="abcd", wordDict=["a", "abc", "b", "cd"]))

# cat, cats, sand, and, dog
