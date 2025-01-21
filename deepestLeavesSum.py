from typing import Optional
from TreeNode import TreeNode, generateBT
from collections import deque


def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    max_level = 0
    leaves_sum = 0
    leaves = []

    # dfs solution
    def dfs(root: TreeNode, depth):
        print(root.val)
        nonlocal max_level, leaves_sum, leaves
        # Reset sum if current depth is deeper than prev depth
        if depth > max_level:
            max_level = depth
            leaves_sum = 0
            leaves = []

        if not root.right and not root.left and depth == max_level:
            leaves_sum += root.val
            leaves.append(root.val)
        if root.left:
            dfs(root.left, depth + 1)
        if root.right:
            dfs(root.right, depth + 1)

    # BFS solution
    cur_l = deque()
    max_level_sum = 0
    cur_l.append(root)
    while cur_l:
        next_l = deque()
        level_sum = 0
        while cur_l:
            node = cur_l.popleft()
            if node.left:
                next_l.append(node.left)
            if node.right:
                next_l.append(node.right)
            level_sum += node.val

        max_level_sum = level_sum
        cur_l = next_l
    return max_level_sum


print(
    deepestLeavesSum(generateBT([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]))
)
print(
    deepestLeavesSum(
        generateBT([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])
    )
)
