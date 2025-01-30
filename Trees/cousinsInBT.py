from collections import deque
from typing import Optional
from utils.TreeNode import TreeNode, generateBT


def isCousins(root: Optional[TreeNode], x: int, y: int) -> bool:
    if not root:
        return False

    q = deque([(root, None)])
    while q:
        c1 = None
        c2 = None
        for _ in range(len(q)):
            cur, parent = q.popleft()
            if cur.val == x:
                c1 = parent
            if cur.val == y:
                c2 = parent
            if parent:
                print(cur.val, parent.val)
            if cur.left:
                q.append((cur.left, cur))
            if cur.right:
                q.append((cur.right, cur))
        if c1 is not None and c2 is not None:
            return c1 != c2
    return False


t = generateBT([1, 2, 3, 4])
print(isCousins(t, t.left.left.val, t.right.val))
t = generateBT([1, 2, 3, None, 4, None, 5])
print(isCousins(t, t.right.right.val, t.left.right.val))
