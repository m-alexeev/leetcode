def mySqrt(x: int) -> int:
    if x == 0:
        return x
    l, r = 1, x
    while l <= r:
        midpoint = l + (r - l) // 2
        if midpoint == x / midpoint:
            return int(midpoint)
        elif midpoint > x / midpoint:
            r = midpoint - 1
        else:
            l = midpoint + 1
    return r


print(mySqrt(1))
print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(16))
