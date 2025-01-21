from typing import List, Optional
from utils.TreeNode import TreeNode


def getMidpoint(nums: List[int]) -> int:
    return len(nums) // 2


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def createTree(nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        midpoint = getMidpoint(nums)
        node = TreeNode(nums[midpoint])
        node.left = createTree(nums[:midpoint])
        node.right = createTree(nums[midpoint + 1 :])
        return node

    if not nums:
        return None
    else:
        return createTree(nums)


print(sortedArrayToBST([-10, -3, 0, 5, 9]))
