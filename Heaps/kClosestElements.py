from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    # find K
    N = len(arr)
    l, r = 0, N - 1

    while l < r:
        m = l + (r - l) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m

    # element outside bounds
    if l >= N:
        return arr[N - k :]
    if l == 0 and arr[l] != x:
        return arr[:k]

    l, r = l - 1, l
    while r - l - 1 < k:
        if l == -1:
            r += 1
        elif r == N or (x - arr[l] <= arr[r] - x):
            l -= 1
        else:
            r += 1
    return arr[l + 1 : r]


print(findClosestElements([1, 2, 3, 4, 5], 4, 4))
print(findClosestElements([1, 1, 1, 10, 10, 10], 1, 9))
print(findClosestElements([1, 1, 2, 3, 4, 5], 4, 6))
