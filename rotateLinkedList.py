from typing import List, Optional
from ListNode import ListNode, generateList


def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if head is None:
        return None

    len_list = 1
    cur = head

    while cur.next != None:
        len_list += 1
        cur = cur.next

    cur.next = head

    k = k % len_list
    for _ in range(len_list - k):
        cur = cur.next
    head = cur.next
    cur.next = None
    return head


print(rotateRight(generateList([1, 2, 3, 4, 5]), 2))
print(rotateRight(generateList([0, 1, 2]), 4))
print(rotateRight(generateList([0, 1]), 2))
