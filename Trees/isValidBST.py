from typing import Optional
from utils.TreeNode import TreeNode, generateBT


def isValidBST(root: Optional[TreeNode]) -> bool:
    def validate(root: Optional[TreeNode]):
        if not root:
            return True, float("inf"), float("-inf")
        # Recursively validate the left and right subtrees
        is_left_valid, left_min, left_max = validate(root.left)
        is_right_valid, right_min, right_max = validate(root.right)

        # Current root validation
        is_valid = (
            is_left_valid
            and is_right_valid
            and (root.left is None or left_max < root.val)
            and (root.right is None or right_min > root.val)
        )

        # Update min and max for the current subtree
        subtree_min = min(root.val, left_min)
        subtree_max = max(root.val, right_max)

        return is_valid, subtree_min, subtree_max

    if not root:
        return True
    else:
        valid, _, _ = validate(root)
        return valid


print(isValidBST(generateBT([2, 1, 3])))
print(isValidBST(generateBT([5, 1, 4, None, None, 3, 6])))
print(isValidBST(generateBT([5, 4, 6, None, None, 3, 7])))
