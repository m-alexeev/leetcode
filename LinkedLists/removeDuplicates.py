from typing import Optional
from utils.ListNode import ListNode, generateList


def removeDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    cur = head
    prev = None
    while cur:
        if cur.next and cur.val == cur.next.val:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if prev is None:
                head = cur.next
            else:
                prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return head


print(removeDuplicates(generateList([1, 2, 3, 3, 4, 4, 5])))
print(removeDuplicates(generateList([1, 1, 1, 2, 3])))
