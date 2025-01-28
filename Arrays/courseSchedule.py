from collections import deque
import re
from typing import List


def courseScheduleII(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    res = []
    map = {}
    pre_req_count = [0] * numCourses
    for course in prerequisites:
        if course[1] not in map:
            map[course[1]] = [course[0]]
        else:
            map[course[1]].append(course[0])
        pre_req_count[course[0]] += 1

    q = deque([i for i in range(numCourses) if pre_req_count[i] == 0])
    while q:
        cur = q.popleft()
        res.append(cur)
        for nextCourse in map.get(cur, []):
            # only add course to list when the count of pre_reqs is 0
            pre_req_count[nextCourse] -= 1
            if pre_req_count[nextCourse] == 0:
                q.append(nextCourse)
    return res if len(res) == numCourses else []


print(courseScheduleII(2, [[1, 0]]))
print(courseScheduleII(1, []))
print(courseScheduleII(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
