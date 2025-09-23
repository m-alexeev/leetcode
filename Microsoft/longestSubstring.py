from collections import Counter


def lengthOfLongestSubstring(s: str) -> int:
    N = len(s)
    if N == 0:
        return 0
    l, r, maxS = 0, 0, 0
    seen = set()
    while r < N:
        if s[r] not in seen:
            seen.add(s[r])
        else:
            print(s[l : r + 1], l, r)
            maxS = max(r - l, maxS)
            while s[l] != s[r] and l < r:
                seen.remove(s[l])
                l += 1
            l += 1
            seen.add(s[r])
        r += 1
    maxS = max(r - l, maxS)
    return maxS


# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbbb"))
# print(lengthOfLongestSubstring("pwwkew"))
#


# Longest substring of length at least k
def longestSubstring(s: str, k: int) -> int:
    longest = 0
    d = Counter(s)
    ignore = [key for key, v in d.items() if v < k]
    ignore = set(ignore)
    cur = 0
    for ch in s:
        if ch in ignore:
            longest = max(longest, cur)
            cur = 0
        else:
            cur += 1
    longest = max(longest, cur)
    return longest


print(longestSubstring("aaabb", 3))  # aaa
print(longestSubstring("aaabbcccc", 3))  # cccc
print(longestSubstring("ababbc", 2))  # ababb

print(longestSubstring("ababacb", 3))  # 0
