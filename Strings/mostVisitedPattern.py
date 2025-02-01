from heapq import heapify
from typing import List
from itertools import combinations
from collections import Counter, defaultdict


def mostVisitedPattern(
    username: List[str], timestamp: List[int], website: List[str]
) -> List[str]:
    user_sites = defaultdict(list)

    tuples = sorted(zip(username, timestamp, website), key=lambda x: x[1])
    for user, _, site in tuples:
        user_sites[user].append(site)
    patterns = Counter()

    for sites in user_sites.values():
        for triplet in set(combinations(sites, 3)):
            patterns[triplet] += 1
    heap = [(-val, key) for key, val in patterns.items()]
    heapify(heap)
    return heap[0][1]


print(
    mostVisitedPattern(
        ["ua", "ua", "ua", "ub", "ub", "ub"],
        [1, 2, 3, 4, 5, 6],
        ["a", "b", "c", "a", "b", "a"],
    )
)
print(
    mostVisitedPattern(
        username=[
            "joe",
            "joe",
            "joe",
            "james",
            "james",
            "james",
            "james",
            "mary",
            "mary",
            "mary",
        ],
        timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        website=[
            "home",
            "about",
            "career",
            "home",
            "cart",
            "maps",
            "home",
            "home",
            "about",
            "career",
        ],
    )
)
