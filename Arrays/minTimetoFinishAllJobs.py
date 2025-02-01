from typing import List
from math import ceil


def minimumTime(jobs: List[int], workers: List[int]) -> int:
    jobs.sort()
    workers.sort()

    minTime = ceil(jobs[0] / workers[0])
    N = len(jobs)
    for i in range(1, N):
        minTime = max(minTime, ceil(jobs[i] / workers[i]))

    return minTime


print(minimumTime([5, 2, 4], [1, 7, 5]))
