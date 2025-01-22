from collections import deque
from typing import List, Optional

from utils.TreeNode import TreeNode, generateBT


def bTreeRightsideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = []
    # DFS implementation
    # def dfs(root, depth):
    #     nonlocal res
    #     if depth == len(res):
    #         res.append(root.val)
    #     if root.right:
    #         dfs(root.right, depth + 1)
    #     if root.left:
    #         dfs(root.left, depth + 1)

    # dfs(root, 0)
    #
    # BFS variant
    q = deque([root])
    while q:
        level_nodes = []
        N = len(q)
        for _ in range(N):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            level_nodes.append(cur.val)
        res.append(level_nodes[-1])
    return res


print(bTreeRightsideView(generateBT([1, 2, 3, None, 5, None, 4])))
print(bTreeRightsideView(generateBT([1, 2, 3, 4, None, None, None, 5])))
