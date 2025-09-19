from __future__ import annotations
from typing import List, Optional


class ListNode:
    val: int = 0
    next: Optional[ListNode] = None

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def createLLFromArray(vals: List[int]) -> Optional[ListNode]:
    if len(vals) == 0:
        return None

    head = ListNode(vals[0])
    cur = head
    for i in range(1, len(vals)):
        node = ListNode(vals[i])
        cur.next = node
        cur = node

    return head


def printList(head: Optional[ListNode]) -> None:
    if not head:
        return
    cur = head
    while cur is not None:
        if cur.next is None:
            print(f"{cur.val}")
        else:
            print(f"{cur.val}", end="->")
        cur = cur.next


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    l = createLLFromArray(a)
    printList(l)
