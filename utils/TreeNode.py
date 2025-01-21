from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}, {self.left}, {self.right}"


def generateBT(items) -> Optional[TreeNode]:

    def inner(items, index) -> Optional[TreeNode]:
        N = len(items)
        if N == 0 or items[index] is None:
            return None

        root = TreeNode(items[index])

        l = 2 * index + 1
        r = 2 * index + 2
        if l < N:
            root.left = inner(items, l)
        if r < N:
            root.right = inner(items, r)
        return root

    return inner(items, 0)
