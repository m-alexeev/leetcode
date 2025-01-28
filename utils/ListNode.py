from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}, {self.next}"


class ListNodeRandom(ListNode):
    def __init__(self, val=0, next=None, random=None) -> None:
        ListNode.__init__(self, val, next)
        self.random = None


def generateList(l: List[int]) -> Optional[ListNode]:
    N = len(l)
    if N == 0:
        return None

    head = ListNode(l[0])
    cur = head
    for i in l[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head
