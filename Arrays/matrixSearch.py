from typing import List


def matrixSearch(matrix: List[List[int]], target: int) -> bool:
    # Binary search the row then the cols since they are each sorted
    def bSearchRows() -> int:
        l, r = 0, len(matrix) - 1
        while l <= r:
            midpoint = l + (r - l) // 2
            if matrix[midpoint][0] <= target <= matrix[midpoint][-1]:
                return midpoint
            elif matrix[midpoint][0] > target:
                r = midpoint - 1
            else:
                l = midpoint + 1
        return -1

    def bSearch(nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            midpoint = l + (r - l) // 2
            if nums[midpoint] == target:
                return midpoint
            if nums[midpoint] < target:
                l = midpoint + 1
            else:
                r = midpoint - 1
        return -1

    row = bSearchRows()
    if row == -1:
        return False
    col = bSearch(matrix[row])
    return col != -1


#
# print(matrixSearch([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0))
# print(matrixSearch([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
# print(matrixSearch([[1, 3]], 3))
print(matrixSearch([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11))
