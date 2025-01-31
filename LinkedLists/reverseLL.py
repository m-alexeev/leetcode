from typing import Optional

from utils.ListNode import ListNode, generateList


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    cur = head
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        if cur.next is None:
            return cur
        else:
            cur = next


print(reverseList(generateList([1, 2, 3, 4, 5])))
