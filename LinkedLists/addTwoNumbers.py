from typing import Optional

from utils.ListNode import ListNode, generateList


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1 and not l2:
        return None

    cur = head = ListNode()
    carry = 0
    while l1 and l2:
        res = l1.val + l2.val + carry
        carry = 1 if res > 9 else 0
        cur.val = res % 10
        l1 = l1.next
        l2 = l2.next
        if l1 and l2:
            cur.next = ListNode()
            cur = cur.next
    if not l1 and not l2 and carry:
        cur.next = ListNode(1)
        return head

    if l1:
        cur.next = l1
    elif l2:
        cur.next = l2
    cur = cur.next

    while l1:
        res = cur.val + carry
        carry = 1 if res > 9 else 0
        cur.val = res % 10
        l1 = l1.next
        if l1:
            cur = cur.next

    while l2:
        res = cur.val + carry
        carry = 1 if res > 9 else 0
        cur.val = res % 10
        l2 = l2.next
        if l2:
            cur = cur.next

    if carry:
        cur.next = ListNode(1)

    return head


print(addTwoNumbers(generateList([2, 4, 3]), generateList([5, 6, 4])))
print(addTwoNumbers(generateList([9, 9, 9]), generateList([9])))
