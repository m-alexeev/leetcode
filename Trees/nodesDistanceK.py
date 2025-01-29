from collections import deque
from typing import List
from utils.TreeNode import TreeNode, generateBT


def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    # Adjacency graph
    adj = {}
    q = deque([(root, None)])
    while q:
        for _ in range(len(q)):
            cur, parent = q.popleft()
            adj[cur.val] = [parent] if parent is not None else []
            if cur.left:
                adj[cur.val].append(cur.left.val)
                q.append((cur.left, cur.val))
            if cur.right:
                adj[cur.val].append(cur.right.val)
                q.append((cur.right, cur.val))

    q = deque([target.val])
    visited = set([target.val])
    nodes = []
    dist = 0
    while q:
        if dist == k:
            return list(q)
        for _ in range(len(q)):
            cur = q.popleft()
            for n in adj[cur]:
                if n not in visited:
                    q.append(n)
                    visited.add(n)
        dist += 1

    return nodes


tree: TreeNode = generateBT([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
target: TreeNode = tree.left
t1 = generateBT([0, 1, 3, None, 2])
ta1 = t1.left
print(distanceK(tree, target, k=2))
print(distanceK(t1, ta1, k=2))
