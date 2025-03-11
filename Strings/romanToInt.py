def romanToInt(s: str) -> int:
    m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    stack = []
    prev = 0
    for i in s:
        stack.append(m[i])

    while stack:
        top = stack.pop()
        if top < prev:
            res -= top
        else:
            res += top
        prev = top

    return res


# print(romanToInt("LVIII"))
# print(romanToInt("MCMXCIV"))


def mapToRoman(i, mult) -> str:
    print(i, mult)
    i_r = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    if i <= 3:
        return i_r[1 * mult] * i
    elif i == 4:
        return i_r[1 * mult] + i_r[5 * mult]
    elif i == 5:
        return i_r[5 * mult]
    elif 5 < i < 9:
        return i_r[5 * mult] + i_r[1 * mult] * (i - 5)
    elif i == 9:
        return i_r[1 * mult] + i_r[mult * 10]
    else:
        return ""


def intToRoman(i: int) -> str:
    s = ""
    if i // 1000 >= 1:
        s += mapToRoman(i // 1000, 1000)
        i %= 1000
    if i // 100 >= 1:
        s += mapToRoman(i // 100, 100)
        i %= 100
    if i // 10 >= 1:
        s += mapToRoman(i // 10, 10)
        i %= 10
    if i < 10:
        s += mapToRoman(i, 1)

    return s


print(intToRoman(11))
print(intToRoman(3749))
