from collections import deque
from typing import List, Optional

from utils.TreeNode import TreeNode, generateBT


def zigzagTravesal(root: Optional[TreeNode]) -> List[List[int]]:

    if root is None:
        return []

    res = []
    q = deque([root])
    level = 1
    while q:
        level_nodes = []
        for _ in range(len(q)):
            if level % 2 == 0:
                cur: TreeNode = q.pop()
                if cur.right:
                    q.appendleft(cur.right)
                if cur.left:
                    q.appendleft(cur.left)
            else:
                cur: TreeNode = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            level_nodes.append(cur.val)
        level += 1
        res.append(level_nodes)
    return res


print(zigzagTravesal(generateBT([3, 9, 20, None, None, 15, 7])))
print(zigzagTravesal(generateBT([1])))
print(zigzagTravesal(generateBT([])))
