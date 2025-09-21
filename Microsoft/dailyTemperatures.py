from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    N = len(temperatures)
    res = [0] * N
    if N == 1:
        return res

    stack = []
    for i in range(N - 1, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures([3, 4, 5]))
print(dailyTemperatures([3, 6, 5]))
