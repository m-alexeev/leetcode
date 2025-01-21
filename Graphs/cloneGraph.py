from typing import Optional
from utils.Node import Node


def cloneGraph(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None

    visitedNodes = {}

    def dfs(root):
        if root in visitedNodes:
            return visitedNodes[root]
        else:
            copy = Node(root.val, [])
            visitedNodes[root] = copy
            for neighbor in root.neighbors:
                newNeighbor = dfs(neighbor)
                if newNeighbor:
                    copy.neighbors.append(newNeighbor)
            return copy

    return dfs(node)
