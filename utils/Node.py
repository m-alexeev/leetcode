from typing import List, Optional


class Node:
    def __init__(self, val, neighbors) -> None:
        self.val = val
        self.neighbors = neighbors
