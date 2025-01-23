from collections import deque
from typing import Optional
from utils.TreeNode import TreeNodeNext, generateBT


def populateNextNode(root: Optional[TreeNodeNext]) -> Optional[TreeNodeNext]:
    if not root:
        return None

    q = deque([root])
    while q:
        next = None
        for _ in range(len(q)):
            cur = q.popleft()
            cur.next = next
            next = cur
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
            print(cur.next)
    return root
