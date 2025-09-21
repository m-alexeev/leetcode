from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


def generateBT(items: List[Optional[int]]) -> Optional[TreeNode]:
    if not items or items[0] is None:
        return None  # No tree to generate

    root = TreeNode(items[0])  # Root of the tree
    queue = deque([root])  # Queue to track nodes at each level
    i = 1  # Start at the first child
    while queue and i < len(items):
        node = queue.popleft()  # Process current node

        # Left child
        if i < len(items) and items[i] is not None:
            node.left = TreeNode(items[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(items) and items[i] is not None:
            node.right = TreeNode(items[i])
            queue.append(node.right)
        i += 1
    return root


def printTree(root: Optional[TreeNode]) -> None:
    if root is None:
        return
    else:
        print(root.val, end=" ")
        printTree(root.left)
        printTree(root.right)


printTree(generateBT([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]))
