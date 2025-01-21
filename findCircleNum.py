from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    N = len(isConnected)
    visited = [False] * N

    num_cons = 0

    def dfs(node):
        for neighbor in range(N):
            if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor)

    for i in range(N):
        if not visited[i]:
            print(num_cons)
            visited[i] = True
            dfs(i)
            num_cons += 1
    return num_cons


print(findCircleNum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
print(findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(findCircleNum([[0, 1, 0], [0, 1, 0], [0, 0, 1]]))
print(findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(findCircleNum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
