from collections import deque
from typing import Optional

from TreeNode import TreeNode, generateBT


def isCompleteTree(root) -> bool:
    q = deque([root])
    while q[0]:
        cur = q.popleft()
        q.extend([cur.left, cur.right])
    print(q)
    while q and not q[0]:
        q.popleft()
    return not q


print(isCompleteTree(generateBT([1, 2, 3, 4, 5])))
print(isCompleteTree(generateBT([1, 2, 3, 4, 5, None, 7])))
print(isCompleteTree(generateBT([1, 2, 3, 5])))
