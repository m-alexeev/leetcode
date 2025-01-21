from typing import Optional
from ListNode import ListNode, generateList


def double(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    prev = None
    while cur != None:
        if cur.val * 2 >= 10:
            cur.val = cur.val * 2 % 10
            if prev is None:
                prev = ListNode(1, cur)
                head = prev
            else:
                prev.val += 1
        else:
            cur.val *= 2
        prev = cur
        cur = cur.next
    return head


print(double(generateList([0, 0, 0])))
print(double(generateList([0, 0, 1])))
print(double(generateList([1])))
print(double(generateList([9, 9, 9])))
