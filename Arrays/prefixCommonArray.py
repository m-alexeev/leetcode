from typing import List


def prefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    seen = set()
    N = len(A)
    res = [0] * N
    for i in range(N):
        count = res[i - 1]
        if A[i] in seen or B[i] in seen:
            count += int(A[i] in seen) + int(B[i] in seen)
        if A[i] == B[i]:
            count += 1
        seen.add(A[i])
        seen.add(B[i])
        res[i] = count
    return res


print(prefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4]))
print(prefixCommonArray(A=[1, 3, 4, 2], B=[3, 1, 2, 4]))
print(prefixCommonArray(A=[2, 3, 1], B=[3, 1, 2]))
print(prefixCommonArray(A=[1, 2, 3], B=[1, 3, 2]))
