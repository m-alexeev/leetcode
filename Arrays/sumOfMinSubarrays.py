from typing import List


def sumSubarrayMins(arr: List[int]) -> int:
    res = [0] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()

        j = stack[-1] if stack else -1
        res[i] = res[j] + (i - j) * arr[i]
        print(res, res[j])

        stack.append(i)

    return sum(res) % (10**9 + 7)


print(sumSubarrayMins([3, 1, 2, 4]))
