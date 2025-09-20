from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    res = []

    def permute(a, l, r):
        if l == r:
            res.append(a[:])
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                permute(a, l + 1, r)
                a[l], a[i] = a[i], a[l]

    permute(nums, 0, len(nums) - 1)
    return res


print(permutations([1, 2, 3]))
