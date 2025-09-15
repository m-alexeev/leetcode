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


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
