from typing import List


def compressString(chars: List[str]) -> int:
    l = 0
    r = 1
    cur_char_count = 1
    N = len(chars)
    while r < N + 1:
        if r == N or chars[r] != chars[r - 1]:
            chars[l] = chars[r - 1]
            l += 1
            if cur_char_count > 1:
                insert = str(cur_char_count)
                for i in range(len(insert)):
                    chars[l] = insert[i]
                    l += 1
            cur_char_count = 1
        else:
            cur_char_count += 1
        r += 1
    print(chars)
    return l


a = ["a", "a", "b", "b", "c", "c", "c"]
print(compressString(a))
b = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(compressString(b))
c = ["a", "a", "a", "a", "a", "b"]
print(compressString(c))
d = ["a", "a", "a", "b", "b", "a", "a"]
print(compressString(d))
