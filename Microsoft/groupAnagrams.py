from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d = {}
    for word in strs:
        sortedWord = "".join(sorted(word))
        print(sortedWord)
        if sortedWord not in d:
            d[sortedWord] = [word]
        else:
            d[sortedWord].append(word)

    return [val for _, val in d.items()]


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
