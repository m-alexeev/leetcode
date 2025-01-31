from collections import deque
from typing import List


def courseSchedule(numCourses: int, prerequisites: List[List[int]]) -> bool:
    if numCourses == 0:
        return True

    # create adjacency graph
    adj_graph = {i: [] for i in range(numCourses)}
    in_degress = {i: 0 for i in range(numCourses)}
    for course, pre_req in prerequisites:
        in_degress[course] += 1
        adj_graph[pre_req].append(course)

    # Look for cycle
    q = deque([i for i in range(numCourses) if in_degress[i] == 0])
    processedNodes = 0
    while q:
        cur = q.popleft()
        processedNodes += 1
        for neighbor in adj_graph[cur]:
            in_degress[neighbor] -= 1
            if in_degress[neighbor] == 0:
                q.append(neighbor)

    return processedNodes == numCourses


print(courseSchedule(2, [[1, 0], [0, 1]]))


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


def courseScheduleIV(
    numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    N = len(prerequisites)
    if N == 0:
        return [False] * len(queries)
    # find nodes without prerequisites
    map = {}
    for i in range(N):
        pre_req, course = prerequisites[i]
        if pre_req in map:
            map[pre_req].append(course)
        else:
            map[pre_req] = [course]
    # get starting course

    def dfs(course, target, visited):
        if course == target:
            return True
        if course not in map:
            return False
        for next in map[course]:
            if next not in visited:
                visited.add(next)
            if dfs(next, target, visited):
                return True
        return False

    res = []
    for course, target in queries:
        res.append(dfs(course, target, set([course])))
    return res


# print(courseScheduleII(2, [[1, 0]]))
# print(courseScheduleII(1, []))
# print(courseScheduleII(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

# print(courseScheduleIV(2, [[1, 0]], [[0, 1], [1, 0]]))
# print(courseScheduleIV(2, [], [[0, 1], [1, 0]]))
# print(courseScheduleIV(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]))
# print(
#     courseScheduleIV(
#         4,
#         [[2, 3], [2, 1], [0, 3], [0, 1]],
#         [[0, 1], [0, 3], [2, 3], [3, 0], [2, 0], [0, 2]],
#     )
# )
