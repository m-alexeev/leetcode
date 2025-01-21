from typing import List


def maxUniqueSubarray(nums: List[int]) -> int:
    N = len(nums)
    cur_window = set()
    max_sum = 0
    l = r = 0
    while r < N:
        if nums[r] not in cur_window:
            cur_window.add(nums[r])
            print(cur_window)
            max_sum = max(sum(cur_window), max_sum)
        else:
            cur_window.remove(nums[l])
            cur_window.add(nums[r])
            l += 1
        r += 1
    return max_sum


print(maxUniqueSubarray([4, 2, 5, 4, 6]))
print(maxUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))
