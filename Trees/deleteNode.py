from typing import Optional
from utils.TreeNode import TreeNode, generateBT


def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return None

    def findMin(node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node.left and not node.right:
            return node
        if node.left:
            return findMin(node.left)
        else:
            return node

    def findAndDeleteNode(node: Optional[TreeNode], parent: Optional[TreeNode]):
        nonlocal key, root
        if not node:
            return
        if key < node.val:
            findAndDeleteNode(node.left, node)
        elif key > node.val:
            findAndDeleteNode(node.right, node)
        else:
            nextNode = None
            if node.right:
                nextNode = findMin(node.right)
            elif node.left:
                # get left node
                nextNode = node.left
            # set the next node of the parent
            if node.val < parent.val:
                parent.left = nextNode
                nextNode.left = node.left
            else:
                parent.right = nextNode

    findAndDeleteNode(root, None)

    return root


print(deleteNode(generateBT([5, 3, 6, 2, 4, None, 7]), 3))
