from typing import Optional
from utils.ListNode import ListNode, generateList


def pairSum(head: Optional[ListNode]) -> int:
    # find middle
    slow = fast = head
    end = head
    while fast:
        end = slow
        slow = slow.next
        fast = fast.next.next

    # Remove node from end
    end.next = None

    # Reverse from
    prev = None
    next = slow.next
    while slow:
        slow.next = prev
        prev = slow
        slow = next
        next = slow.next if slow else None

    head2 = prev
    # Find max
    mx = 0
    while head and head2:
        mx = max(head.val + head2.val, mx)
        head = head.next
        head2 = head2.next
    return mx


print(pairSum(generateList([5, 4, 2, 1])))
print(pairSum(generateList([1, 2])))
