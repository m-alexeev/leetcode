def minFlipsMonoIncr(s: str) -> int:
    ans = 0
    num = 0
    for c in s:
        if c == "0":
            ans = min(num, ans + 1)
        else:
            num += 1
    return ans


print(minFlipsMonoIncr("00110"))
print(minFlipsMonoIncr("010110"))
print(minFlipsMonoIncr("00011000"))
