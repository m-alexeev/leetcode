def longestPalindrom(s: str) -> str:
    N = len(s)
    maxP = ""

    for i in range(N):
        l = r = i
        while l >= 0 and r < N and s[l] == s[r]:
            if r - l >= len(maxP):
                maxP = s[l : r + 1]
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < N and s[l] == s[r]:
            if r - l >= len(maxP):
                maxP = s[l : r + 1]
            l -= 1
            r += 1
    return maxP


print(longestPalindrom("abac"))
print(longestPalindrom("babad"))
print(longestPalindrom("cbbd"))
print(longestPalindrom("ac"))
print(longestPalindrom("cc"))
print(longestPalindrom("ccd"))
print(longestPalindrom("ccc"))
print(longestPalindrom("accc"))
