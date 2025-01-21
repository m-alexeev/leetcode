def countPrimes(n: int) -> int:
    nums = [False for i in range(n)]
    count = 0
    for i in range(2, n):
        if nums[i] == False:
            count += 1

        for j in range(i, len(nums), i):
            nums[j] = True

    print(nums)
    return count


print(countPrimes(10))
