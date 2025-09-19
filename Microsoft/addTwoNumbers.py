from ListNode import ListNode, printList, createLLFromArray
from typing import Optional


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 is None and l2 is None:
        return None
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    carry, cur, head = 0, None, None
    while l1 is not None and l2 is not None:
        s = l1.val + l2.val + carry
        if s > 9:
            carry = 1
            s = s % 10
        else:
            carry = 0

        if head is None:
            head = ListNode(s)
            cur = head
        else:
            node = ListNode(s)
            cur.next = node
            cur = node

        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        s = l1.val + carry
        if s > 9:
            carry = 1
            s = s % 10
        else:
            carry = 0

        if head is None:
            head = ListNode(s)
            cur = head
        else:
            node = ListNode(s)
            cur.next = node
            cur = node
        l1 = l1.next

    while l2 is not None:
        s = l2.val + carry
        if s > 9:
            carry = 1
            s = s % 10
        else:
            carry = 0

        if head is None:
            head = ListNode(s)
            cur = head
        else:
            node = ListNode(s)
            cur.next = node
            cur = node
        l2 = l2.next

    if carry:
        node = ListNode(carry)
        cur.next = node
        cur = node
    return head


l1 = createLLFromArray([2, 4, 9])
l2 = createLLFromArray([5, 6, 4, 9])
printList(addTwoNumbers(l1, l2))

# l1 = createLLFromArray([9, 9, 9])
# l2 = createLLFromArray([9, 9])
# printList(addTwoNumbers(l1, l2))
