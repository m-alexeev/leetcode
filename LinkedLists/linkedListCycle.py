from typing import Optional
from utils.ListNode import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    slow = head
    fast = head.next
    while fast != None and fast.next != None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
