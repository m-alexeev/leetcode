def factorialTrailingZeros(n: int) -> int:
    l = 0
    r = n
    tens = 0
    fives = 0
    twos = 0
    while l <= r:
        # Count factors for l
        temp_l = l
        while temp_l % 10 == 0 and temp_l > 0:  # Count multiples of 10
            tens += 1
            temp_l //= 10
        while temp_l % 5 == 0 and temp_l > 0:  # Count multiples of 5
            fives += 1
            temp_l //= 5
        while temp_l % 2 == 0 and temp_l > 0:  # Count multiples of 2
            twos += 1
            temp_l //= 2
        l += 1

        # Count factors for r (only if l < r to avoid double counting)
        if l < r:
            temp_r = r
            while temp_r % 10 == 0 and temp_r > 0:  # Count multiples of 10
                tens += 1
                temp_r //= 10
            while temp_r % 5 == 0 and temp_r > 0:  # Count multiples of 5
                fives += 1
                temp_r //= 5
            while temp_r % 2 == 0 and temp_r > 0:  # Count multiples of 2
                twos += 1
                temp_r //= 2
        r -= 1

    # Total trailing zeros are determined by the limiting factor (5 or 2), plus tens
    return tens + min(twos, fives)


print(factorialTrailingZeros(15))
print(factorialTrailingZeros(101))
# print(factorialTrailingZeros(45))
# print(factorialTrailingZeros(100))
print(factorialTrailingZeros(1000))
