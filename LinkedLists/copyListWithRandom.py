from typing import Optional
from utils.ListNode import ListNodeRandom


def copyRandomList(head: Optional[ListNodeRandom]) -> Optional[ListNodeRandom]:
    # Create copies of list
    cur = head
    if cur is None:
        return None

    new_head = ListNodeRandom(cur.val)
    new_cur = new_head
    while cur.next != None:
        cur = cur.next
        new_cur.next = ListNodeRandom(cur.val)
        new_cur = new_cur.next
