def lengthOfLastWord(s: str) -> int:
    l = 0
    i = len(s) - 1
    while i >= 0:
        if s[i] == " ":
            if l > 0:
                return l
        else:
            l += 1
        i -= 1
    return l


print(lengthOfLastWord("   fly me   to   the moon  "))
