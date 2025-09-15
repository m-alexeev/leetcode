from typing import List


def twoSum(arr: List[int], target: int) -> List[int]:
    d = {}
    for i, num in enumerate(arr):
        if num in d:
            return [i, d[num]]
        else:
            d[target - num] = i
    return [0, 0]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
