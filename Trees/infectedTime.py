from collections import deque
from typing import Optional
from utils.TreeNode import TreeNode, generateBT


def amountOfTime(root: Optional[TreeNode], start: int) -> int:
    time = 0
    if not root:
        return 0

    relationships = {}

    q = deque([(root, None)])
    parent = None
    while q:
        cur = None
        for _ in range(len(q)):
            cur, parent = q.popleft()
            if parent is not None:
                relationships[cur.val] = [parent]
            else:
                relationships[cur.val] = []
            if cur.left:
                relationships[cur.val].append(cur.left.val)
                q.append((cur.left, cur.val))
            if cur.right:
                relationships[cur.val].append(cur.right.val)
                q.append((cur.right, cur.val))

    # infect
    visited = set()
    visited.add(start)
    q = deque([start])
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            for neighbor in relationships[cur]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        print(q)
        if q:
            time += 1

    return time


print(amountOfTime(generateBT([1, 5, 3, None, 4, 10, 6, 9, 2]), 3))
print(amountOfTime(generateBT([1]), 1))
print(amountOfTime(generateBT([1, 2, None, 3, None, 4, None, 5]), 3))
