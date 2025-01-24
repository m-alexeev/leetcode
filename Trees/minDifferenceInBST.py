from typing import Optional
from utils.TreeNode import TreeNode, generateBT


def getMinimumDifference(root: Optional[TreeNode]) -> int:
    m = prev = float("inf")

    def inOrder(node: Optional[TreeNode]):
        nonlocal m, prev
        if not node:
            return
        inOrder(node.left)
        m, prev = min(m, abs(prev - node.val)), node.val
        inOrder(node.right)

    inOrder(root)
    print(m)
    return int(m)


getMinimumDifference(generateBT([4, 2, 6, 1, 3]))
getMinimumDifference(generateBT([236, 104, 701, None, 227, None, 911]))
