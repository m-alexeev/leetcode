from typing import List


def distinctElements(nums: List[int], k: int) -> List[int]:
    N = len(nums)
    hash = {}
    l = 0
    uniq = []
    elems = 0
    for r in range(N):
        if nums[r] in hash:
            hash[nums[r]] += 1
        else:
            hash[nums[r]] = 1
            elems += 1
        if r - l + 1 > k:
            if nums[l] in hash:
                if hash[nums[l]] > 1:
                    hash[nums[l]] -= 1
                else:
                    del hash[nums[l]]
                    elems -= 1
                l += 1
            uniq.append(elems)
        if r == k - 1:
            uniq.append(elems)
        print(hash, elems)
    return uniq


print(distinctElements([1, 2, 3, 2, 2, 1, 3], 3))
print(distinctElements(nums=[1, 1, 1, 1, 2, 3, 4], k=4))
