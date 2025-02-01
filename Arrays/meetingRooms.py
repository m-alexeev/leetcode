from typing import List
from heapq import heappush, heappop


def minMeetingRoomsII(intervals: List[List[int]]) -> int:
    N = len(intervals)
    minRooms = 0
    if N == 0:
        return minRooms

    intervals.sort()
    heap = []
    for interval in intervals:
        start, end = interval
        if not heap:
            heappush(heap, end)
        else:
            while heap and start >= heap[0]:
                heappop(heap)
            heappush(heap, end)
        print(heap)
        minRooms = max(minRooms, len(heap))
    return minRooms


print(minMeetingRoomsII([[0, 30], [5, 10], [15, 20]]))
print(minMeetingRoomsII([[5, 30], [10, 25], [15, 25], [20, 45]]))
print(minMeetingRoomsII([[7, 10], [2, 4]]))
