from typing import List


def hIndex(citations: List[int]) -> int:
    num_cits = [0] * (max(citations) + 1)
    for i in citations:
        num_cits[i] += 1

    count = 0
    for i in range(len(num_cits) - 1, -1, -1):
        count += num_cits[i]
        if count >= i:
            return i

    return 0


print(hIndex([3, 0, 6, 1, 5]))
print(hIndex([1, 3, 1]))
