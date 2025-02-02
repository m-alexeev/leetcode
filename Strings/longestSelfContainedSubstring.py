from collections import Counter


def maxSubstringLength(s: str) -> int:
    N = len(s)
    hashmap = Counter(s)
    l, r = 0, N - 1
    maxLen = 0
    outside = set()
    while l <= r:
        if hashmap[s[l]] > 1:
            hashmap[s[l]] -= 1
            l += 1
        elif hashmap[s[r]] > 1:
            hashmap[s[r]] -= 1
            r -= 1
        else:
            maxLen = max(maxLen, r - l + 1)
            break  # Stop once we have a valid substring
    return maxLen


print(maxSubstringLength("abba"))
print(maxSubstringLength("abab"))
print(maxSubstringLength("abacd"))
