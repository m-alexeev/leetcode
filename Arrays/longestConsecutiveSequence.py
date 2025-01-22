from typing import List


def longestSequence(nums: List[int]) -> int:
    if not nums:
        return 0
    s = set(nums)

    max_streak = 0
    for i in s:
        if i - 1 not in s:
            cur = i
            streak = 1
            while cur + 1 in s:
                streak += 1
                cur += 1
            max_streak = max(streak, max_streak)

    return max_streak


print(longestSequence([100, 4, 200, 1, 3, 2]))
print(longestSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
