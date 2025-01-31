from typing import List


def trapRainWater(height: List[int]) -> int:
    trapped = 0
    maxL = maxR = 0
    N = len(height)
    l, r = 0, N - 1
    res = [0] * N
    while l < r:
        if maxL < maxR:
            l += 1
            maxL = max(maxL, height[l])
            trapped += maxL - height[l]
        else:
            r -= 1
            maxR = max(maxL, height[r])
            trapped += maxR - height[r]

    print(res)
    return trapped


print(trapRainWater(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trapRainWater(height=[2, 1, 0, 0, 1, 3, 1, 0, 3, 0, 0, 2, 1, 1, 2]))
# print(trapRainWater(height=[4, 2, 0, 3, 2, 5]))
