from heapq import heapify
from utils.ListNode import DoubleListNode, ListNode


class LRUCache:

    def __init__(self, size) -> None:
        self.head = DoubleListNode(0, 0)
        self.tail = DoubleListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {}
        self.size = size

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            # move node to head
            self.removeNode(node)
            self.insertHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.removeNode(node)
            self.insertHead(node)
        else:
            if len(self.map) >= self.size:
                self.removeTail()
            node = DoubleListNode(value, key)
            self.map[key] = node
            self.insertHead(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertHead(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def removeTail(self):
        if len(self.map) == 0:
            return
        tailNode = self.tail.prev
        del self.map[tailNode.key]
        self.removeNode(tailNode)


cache = LRUCache(2)
cache.put(1, 0)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
