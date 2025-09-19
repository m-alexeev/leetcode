from __future__ import annotations
from typing import Dict


class Node:
    key: int
    val: int

    def __init__(self, key: int, val: int, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity) -> None:
        self.head: Node = Node(0, 0)
        self.tail: Node = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cap = capacity
        self.nodes: Dict[int, Node] = {}

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.removeNode(self.nodes[key])
            self.addToHead(self.nodes[key])
            return self.nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key].val = value
            self.removeNode(self.nodes[key])
            self.addToHead(self.nodes[key])
        else:
            node = Node(key, value)
            self.nodes[key] = node
            self.addToHead(node)
            if len(self.nodes.keys()) - 1 == self.cap:
                self.removeTail()

    def removeNode(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node: Node):
        headNext = self.head.next
        self.head.next = node
        node.next = headNext
        node.prev = self.head
        headNext.prev = node

    def removeTail(self):
        if len(self.nodes) == 0:
            return
        tailNode = self.tail.prev
        del self.nodes[tailNode.key]
        self.removeNode(tailNode)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.head.val)
print(cache.tail.val)
