from typing import List


def minimumCardPickup(cards: List[int]) -> int:
    seen = {}
    min_consec = 10**5 + 1
    for i, card in enumerate(cards):
        if card in seen:
            min_consec = min(min_consec, i - seen[card] + 1)
        else:
            seen[card] = i
    if min_consec < 10**5:
        return min_consec
    else:
        return -1


print(minimumCardPickup([3, 4, 2, 3, 4, 7]))
print(minimumCardPickup([1, 0, 5, 3]))
