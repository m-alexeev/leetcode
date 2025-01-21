from typing import Optional
from utils.TreeNode import TreeNode


def lowestCommonAncestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    if not root or root == p or root == q:
        return root

    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)

    if l and r:
        return root
    return l or r
