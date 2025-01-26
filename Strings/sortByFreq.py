def frequencySort(s: str) -> str:
    # naive
    h = {}
    for c in s:
        if c in h:
            h[c] += 1
        else:
            h[c] = 1

    # sorted_h = [k * v for k, v in sorted(h.items(), key=lambda kv: kv[1], reverse=True)]
    # return "".join(sorted_h)

    # hash + bucket
    buckets = [[] for i in range(len(s) + 1)]
    print(buckets)
    for k, v in h.items():
        buckets[v].append(k)

    res = ""
    for i in range(len(buckets) - 1, -1, -1):
        for char in buckets[i]:
            res += char * i

    return res


print(frequencySort("abcabcdecbb"))
print(frequencySort("aaaaa"))
