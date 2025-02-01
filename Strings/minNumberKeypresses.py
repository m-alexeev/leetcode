from heapq import heapify, heappop


def minimumKeypresses(s: str) -> int:
    presses = 0
    N = len(s)
    if N == 0:
        return presses

    heap = [[0, chr(i + 97)] for i in range(26)]
    for i in s:
        heap[ord(i) - 97][0] -= 1
    heapify(heap)
    print(heap)
    keypad = {1: [0, 0], 2: [0, 0], 3: [0, 0]}
    while heap:
        occurance, _ = heappop(heap)
        if occurance == 0:
            continue
        if keypad[1][0] < 9:
            keypad[1][0] += 1
            keypad[1][1] += -occurance
        elif keypad[2][0] < 9:
            keypad[2][0] += 1
            keypad[2][1] += -occurance * 2
        else:
            keypad[3][0] += 1
            keypad[3][1] += -occurance * 3

    return sum([keypad[1][1], keypad[2][1], keypad[3][1]])


print(minimumKeypresses("apple"))
print(minimumKeypresses("abcdefghijkl"))
