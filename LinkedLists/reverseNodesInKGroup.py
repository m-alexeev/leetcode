from typing import Optional

from utils.ListNode import ListNode, generateList


def reverseList(head: Optional[ListNode], k) -> Optional[ListNode]:
    cur = head
    prev = None
    while k > 0:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

        k -= 1
    return prev


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return

    cur = head
    tail = None
    prev = None

    while cur is not None:
        count = 0

        cur = head
        while count < k and cur is not None:
            cur = cur.next
            count += 1

        if count == k:
            reversed = reverseList(head, k)

            if prev == None:
                prev = reversed

            if tail is not None:
                tail.next = reversed

            tail = head
            head = cur

    if tail is not None:
        tail.next = head

    return prev if prev is not None else head


print(reverseKGroup(generateList([1, 2, 3, 4, 5]), 3))
