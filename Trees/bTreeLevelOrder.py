from collections import deque
from typing import List, Optional

from utils.TreeNode import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        level = []
        for i in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            level.append(cur.val)
        res.append(level)

    return res
