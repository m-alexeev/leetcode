from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = set()

    def backtrack(arr, target, start):
        nonlocal res
        if target == 0:
            res.add(tuple(arr))
        elif target < 0:
            return
        for i in range(start, len(candidates)):
            backtrack(arr + [candidates[i]], target - candidates[i], i)

    backtrack([], target, 0)
    return list([list(s) for s in res])


print(combinationSum([2, 3, 6, 7], 7))
