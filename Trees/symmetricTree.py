from typing import Optional

from utils.TreeNode import TreeNode, generateBT


def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return False

    def check(left, right):
        if left is None and right is None:
            return True
        if left is None and right is not None:
            return False
        if left is not None and right is None:
            return False
        return (
            left.val == right.val
            and check(left.left, right.right)
            and check(left.right, right.left)
        )

    return check(root.left, root.right)


print(isSymmetric(generateBT([1, 2, 2, 3, 4, 4, 3])))
print(isSymmetric(generateBT([1, 2, 2, None, 3, None, 3])))
print(isSymmetric(generateBT([1, 2, 2, 2, None, 2])))
