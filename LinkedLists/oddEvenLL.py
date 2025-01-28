from typing import Optional
from utils.ListNode import ListNode, generateList


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next or not head.next.next:
        return head

    even = head
    oddHead = even.next
    odd = even.next
    while even.next and odd.next:
        even.next = odd.next
        even = even.next
        odd.next = even.next
        odd = odd.next

    even.next = oddHead
    return head


print(oddEvenList(generateList([1, 2, 3, 4, 5, 6])))
print(oddEvenList(generateList([1, 2, 3])))
print(oddEvenList(generateList([1])))
