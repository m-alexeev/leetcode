from typing import Optional
from utils.ListNode import ListNode, generateList


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1 and not list2:
        return None
    if not list1 or not list2:
        return list1 if list1 else list2

    head = list1 if list1.val <= list2.val else list2
    if head == list1:
        list1 = list1.next
    else:
        list2 = list2.next
    tail = head

    while list1 and list2:
        if list1.val > list2.val:
            tail.next = list2
            list2 = list2.next
        else:
            tail.next = list1
            list1 = list1.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return head


l1 = generateList([1, 2, 4])
l2 = generateList([1, 3, 4])
print(mergeTwoLists(l1, l2))
l1 = generateList([1, 2])
l2 = generateList([1, 3, 4])
print(mergeTwoLists(l1, l2))
l1 = generateList([1, 2, 3])
l2 = generateList([1, 3])
print(mergeTwoLists(l1, l2))
