def myPow(x: float, n: int) -> int:

    def pow(res, n):
        if n == 0:
            return 1
        else:
            return res * pow(res, n - 1)

    if n < 0:
        return 1 / pow(x, -n)
    else:
        return pow(x, n)


print(myPow(2, 10))
print(myPow(2.1, 3))
print(myPow(2, -2))
