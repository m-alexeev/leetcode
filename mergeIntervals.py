from typing import List


def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    intervals.sort()
    if intervals:
        merged.append(intervals[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(intervals[i][1], merged[-1][1])
        else:
            merged.append(intervals[i])
    return merged


print(mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(mergeIntervals([[1, 4], [2, 3]]))
