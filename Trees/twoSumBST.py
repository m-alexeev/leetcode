from typing import Optional
from utils.TreeNode import TreeNode, generateBT


def twoSumBST(root: Optional[TreeNode], k: int) -> int:
    arr = []

    def inOrder(node: Optional[TreeNode]):
        nonlocal arr
        if not node:
            return
        if node.left:
            inOrder(node.left)
        arr.append(node.val)
        if node.right:
            inOrder(node.right)

    inOrder(root)
    l, r = 0, len(arr) - 1

    while l < r:
        if arr[l] + arr[r] == k:
            return True
        if arr[l] + arr[r] < k:
            l += 1
        else:
            r -= 1
    return False


print(twoSumBST(generateBT([5, 3, 6, 2, 4, None, 7]), 2))
print(twoSumBST(generateBT([1]), 2))
