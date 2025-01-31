from typing import Optional
from utils.ListNode import ListNodeRandom as Node


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    cur = head
    if cur is None:
        return None

    # duplicate list
    cur = head
    while cur:
        node = Node(cur.val)
        node.next = cur.next
        cur.next = node
        cur = node.next

    # create the random pointers
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next

    # remove duplicate from list
    copyHead = head.next
    copyCur = copyHead
    cur = head
    while cur:
        cur.next = cur.next.next
        if copyCur.next:
            copyCur.next = copyCur.next.next
        cur = cur.next
        copyCur = copyCur.next

    return copyHead
