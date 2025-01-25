def lengthOfLongestSubstring(s: str) -> int:

    N = len(s)
    if N == 0:
        return 0
    l, r, max_len = 0, 0, 1
    seen = set()
    while r < N:
        if s[r] in seen:
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    break
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
        else:
            seen.add(s[r])
        r += 1
        max_len = max(max_len, r - l)
    return max_len


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("abc"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("tmmzuxt"))
