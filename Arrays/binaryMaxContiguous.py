from typing import List


def findMaxLength(nums: List[int]) -> int:
    prefix_sum = max_length = 0
    h = {0: -1}
    for idx, num in enumerate(nums):
        prefix_sum += 1 if num == 1 else -1

        if prefix_sum in h:
            max_length = max(max_length, idx - h[prefix_sum])
        else:
            h[prefix_sum] = idx

    return max_length


print(findMaxLength([0, 1]))
print(findMaxLength([0, 1, 0]))
print(findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]))
print(findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))
