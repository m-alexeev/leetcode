from typing import Optional
from utils.TreeNode import TreeNode, generateBT


def invert(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    left = right = None
    if root.left:
        left = invert(root.left)
    if root.right:
        right = invert(root.right)
    root.left = right
    root.right = left
    return root


print(invert(generateBT([2, 1, 3])))
