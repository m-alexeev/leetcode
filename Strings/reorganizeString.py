from heapq import heapify, heappush, heappop


def reorganizeString(s: str) -> str:
    occurances = {}
    for i in s:
        occurances[i] = occurances.get(i, 0) + 1

    heap = [(-count, char) for char, count in occurances.items()]
    heapify(heap)

    res = ""
    prev = None

    while heap:
        count, char = heappop(heap)
        res += char

        if prev:
            heappush(heap, prev)
            prev = None

        if count + 1 < 0:
            prev = (count + 1, char)
    return res if len(res) == len(s) else ""


print(reorganizeString("aab"))
print(reorganizeString("vvvlo"))
print(reorganizeString("aaabbc"))
print(reorganizeString("aaaaabbbbccc"))
