from typing import List


def subsets(nums: List[int]) -> List[List[int]]:

    res = [[]]

    def backtrack(sub, arr: List[int]):
        for i in range(len(arr)):
            sub.append(arr[i])
            res.append(sub[:])
            backtrack(sub, arr[i + 1 :])
            sub.pop()

    backtrack([], nums)
    return res


print(subsets([1, 2, 3]))
print(subsets([1]))
