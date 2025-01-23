def wordPattern(pattern: str, s: str) -> bool:
    words = s.split(" ")
    if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
        return False
    d = {}
    for i, char in enumerate(pattern):
        if char in d:
            if d[char] != words[i]:
                return False
        else:
            d[char] = words[i]
    print(d)
    return True


print(wordPattern("abba", "dog dog dog dog"))
print(wordPattern("abab", "cat dog cat dog"))
