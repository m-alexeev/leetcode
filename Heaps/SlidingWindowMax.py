from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    N = len(nums)
    res = []
    if N == 0:
        return res

    # Brute force
    # for i in range(N - k + 1):
    #     res.append(max(nums[i : i + k]))

    # Optimize
    q = deque([])
    l = r = 0
    while r < N:
        if r - l == k:
            # remove last elem from queue
            if q[0][1] <= l:
                res.append(q.popleft()[0])
            else:
                res.append(q[0][0])
            l += 1
        else:
            while q and q[-1][0] < nums[r]:
                q.pop()
            q.append((nums[r], r))
            r += 1
        # print(q)

    return res + [q[0][0]]


print(maxSlidingWindow([4, 2, 3, 1, 2], 3))
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(maxSlidingWindow([1, -1], 1))
print(maxSlidingWindow([1], 1))
