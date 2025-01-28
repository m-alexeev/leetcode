from typing import List


def jumpGameII(nums: List[int]) -> int:
    N = len(nums)
    jumps = max_end = cur_end = 0
    for i in range(N - 1):
        max_reach = nums[i] + i
        max_end = max(max_end, max_reach)
        if i == cur_end:
            jumps += 1
            cur_end = max_end
        print(cur_end, max_end, jumps)
    return jumps


print(jumpGameII([2, 3, 1, 1, 4]))
print(jumpGameII([2, 3, 0, 1, 4]))
print(jumpGameII([4, 1, 1, 3, 1, 1, 1]))
print(jumpGameII([1, 1, 1, 1]))
