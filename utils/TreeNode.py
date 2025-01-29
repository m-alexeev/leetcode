from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}, {self.left}, {self.right}"


class TreeNodeNext(TreeNode):
    def __init__(self, val=0, left=None, right=None, next=None) -> None:
        TreeNode.__init__(self, val, left, right)
        self.next = next


def generateBT(items) -> Optional[TreeNode]:
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
