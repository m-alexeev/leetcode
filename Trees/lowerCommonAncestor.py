from utils.TreeNode import TreeNode, generateBT
from typing import List, Optional


def lowestCommonAncestor(root: TreeNode, nodes: List[TreeNode]) -> TreeNode:
    nodes = set(nodes)
    common = None

    def dfs(root: Optional[TreeNode]):
        nonlocal common, nodes
        if not root:
            return False
        l = dfs(root.left)
        r = dfs(root.right)
        found = root in nodes
        if found or (l and r):
            common = root
        return found or (l and r)

    dfs(root)

    return common


t = generateBT([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(lowestCommonAncestor(t, [t.left.right.left, t.left.right.right]))
t = generateBT([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(lowestCommonAncestor(t, [t.right]))
t = generateBT([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(
    lowestCommonAncestor(
        t, [t.left.left, t.left.right, t.left.right.left, t.left.right.right]
    )
)
