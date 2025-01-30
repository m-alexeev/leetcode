from typing import List


def combinationSumII(candidates: List[int], target: int) -> List[List[int]]:

    res = set()
    candidates.sort()
    N = len(candidates)

    def backtrack(cur, start, t):
        nonlocal N
        if t < 0:
            return
        if t == 0:
            res.add(tuple(cur))
            return
        for i in range(start, N):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            cur.append(candidates[i])
            backtrack(cur, i + 1, t - candidates[i])
            cur.pop()

    backtrack([], 0, target)
    return [list(r) for r in res]


print(combinationSumII(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
# print(combinationSum(candidates=[2, 5, 2, 1, 2], target=5))
