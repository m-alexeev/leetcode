from typing import List


def trappingRainWater(height: List[int]) -> int:
    leftMax = height[0]
    rightMax = height[-1]

    l, r = 0, len(height) - 1
    trap = 0
    while l < r:
        if leftMax <= rightMax:
            trap += leftMax - height[l]
            l += 1
            leftMax = max(leftMax, height[l])
        else:
            trap += rightMax - height[r]
            r -= 1
            rightMax = max(rightMax, height[r])

    return trap


print(trappingRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trappingRainWater(height=[4, 2, 0, 3, 2, 5]))
