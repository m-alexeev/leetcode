def reverseInteger(x: int) -> int:
    sign = 1 if x > 0 else -1
    res, i, limit, x = 0, 0, 2**31 - 1, abs(x)
    while x > 0:
        n = x % 10
        x //= 10
        i += 1
        if res > limit // 10:
            return 0
        res = (res * 10) + n

    return res * sign


print(reverseInteger(7))
print(reverseInteger(17))
print(reverseInteger(120))
print(reverseInteger(-120))
