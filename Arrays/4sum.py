from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:

    def threeSum(arr, target):
        threes = []
        for i in range(len(arr) - 2):
            l = i + 1
            r = len(arr) - 1
            t = target - arr[i]
            if i == 0 or arr[i] != arr[i - 1]:
                while l < r:
                    s = arr[l] + arr[r]
                    if s == t:
                        threes.append([arr[i], arr[l], arr[r]])
                        while l < r and arr[l] == arr[l + 1]:
                            l += 1
                        while l < r and arr[r] == arr[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < t:
                        l += 1
                    else:
                        r -= 1
        return threes

    res = []
    nums.sort()
    for i in range(len(nums) - 3):
        if i == 0 or nums[i] != nums[i - 1]:
            three = threeSum(nums[i + 1 :], target - nums[i])
            for j in three:
                res.append(j + [nums[i]])
    return res


print(fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
