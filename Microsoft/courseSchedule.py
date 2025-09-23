from collections import deque
from typing import List


def courseScheduleII(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    coursePreReqs = {}
    preReqCount = [0] * numCourses
    for c, req in prerequisites:
        if req in coursePreReqs:
            coursePreReqs[req].append(c)
        else:
            coursePreReqs[req] = [c]
        preReqCount[c] += 1
    frontier = deque([i for i in range(numCourses) if preReqCount[i] == 0])
    res = []
    while frontier:
        cur = frontier.popleft()
        res.append(cur)
        for nextCourse in coursePreReqs.get(cur, []):
            preReqCount[nextCourse] -= 1
            if preReqCount[nextCourse] == 0:
                frontier.append(nextCourse)

    return res if len(res) == numCourses else []


print(courseScheduleII(2, [[1, 0], [0, 1]]))
print(courseScheduleII(2, [[0, 1]]))
print(courseScheduleII(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
