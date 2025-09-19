from typing import List


def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1:
        return intervals
    # Sort by end
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    res = []
    cur = sortedIntervals[0]
    for i in sortedIntervals[1:]:
        print(i)
        if i[0] <= cur[1]:
            cur[1] = max(i[1], cur[1])
        else:
            res.append(cur)
            cur = i
    res.append(cur)
    return res


print(mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(mergeIntervals([[1, 4], [4, 5]]))
