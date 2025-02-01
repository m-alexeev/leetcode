from typing import List


def minimumSwaps(nums: List[int]) -> int:
    N = len(nums)
    if N < 2:
        return 0

    # Find smallest and largest numbers closest to ends
    smallest = [10**5, N]
    largest = [0, 0]
    for i in range(N):
        if nums[i] < smallest[0]:
            smallest = [nums[i], i]
        if nums[i] >= largest[0]:
            largest = [nums[i], i]

    if smallest[0] == largest[0]:
        return 0
    # if intersecting, one less swap
    if smallest[1] > largest[1]:
        return smallest[1] + ((N - 1) - largest[1] - 1)
    else:
        return smallest[1] + ((N - 1) - largest[1])


print(minimumSwaps([3, 1, 5, 5, 3, 3]))
