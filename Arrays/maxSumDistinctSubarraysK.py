from typing import List


def maximumSubarraySum(nums: List[int], k: int) -> int:
    maxSum = 0
    subarray = set()
    N = len(nums)
    l = r = 0
    curSum = 0
    while r < N:
        curSum += nums[r]
        while nums[r] in subarray:
            curSum -= nums[l]
            subarray.remove(nums[l])
            l += 1
        else:
            subarray.add(nums[r])
        if r - l == k - 1:
            maxSum = max(curSum, maxSum)
            curSum -= nums[l]
            subarray.remove(nums[l])
            l += 1
        r += 1
        pass

    return maxSum


print(maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
print(maximumSubarraySum([4, 4, 4], 3))
