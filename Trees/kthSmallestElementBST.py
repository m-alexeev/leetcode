from typing import Optional
from utils.TreeNode import TreeNode, generateBT


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    res = 0
    count = k

    def inOrder(root: Optional[TreeNode]):
        nonlocal count, res
        if not root:
            return
        inOrder(root.left)
        if count > 0:
            res = root.val
            count -= 1
        if count > 0:
            inOrder(root.right)

    inOrder(root)
    return res


print(kthSmallest(generateBT([3, 1, 4, None, 2]), 1))
