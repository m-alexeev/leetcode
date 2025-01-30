from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    N = len(gas)
    if sum(gas) < sum(cost):
        return -1
    gas_left = start = 0

    for i in range(N):
        gas_left += gas[i] - cost[i]
        if gas_left < 0:
            start = i + 1
            gas_left = 0
    return start


print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))
