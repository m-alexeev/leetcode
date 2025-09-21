from typing import Optional

from Microsoft.ListNode import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    if not head.next:
        return False

    slow, fast = head, head.next

    while True:
        if slow == fast:
            return True
        if fast.next and fast.next.next:
            fast = fast.next.next
        slow = slow.next
