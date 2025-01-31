from heapq import heapify, heappop
from typing import List, Optional
from utils.ListNode import ListNode, generateList


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []

    index = 0
    for l in lists:
        cur = l
        while cur:
            next = cur.next
            cur.next = None
            heap.append((cur.val, index, cur))
            cur = next
            index += 1

    heapify(heap)
    if not heap:
        return
    _, _, head = heappop(heap)
    cur = head

    while heap:
        _, _, node = heappop(heap)
        cur.next = node
        cur = node
    cur.next = None
    return head


print(
    mergeKLists(
        [generateList([1, 4, 5]), generateList([1, 3, 4]), generateList([2, 6])]
    )
)
print(mergeKLists([]))
