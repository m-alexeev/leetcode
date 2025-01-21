def myAtoi(s: str):
    sign = 1
    res = 0
    res_str = ""
    dig_char = False
    sign_char = False
    for ch in s:
        if ch == " " and len(res_str) == 0 and not sign_char and not dig_char:
            continue
        if ch in "+-":
            if dig_char:
                break
            else:
                if sign_char:
                    return 0
                else:
                    sign = [-1, 1][ch == "+"]
            sign_char = True
        elif ch.isdigit():
            dig_char = True
            res_str += ch
        else:
            if dig_char:
                break
            else:
                return 0

    for i, ch in enumerate(res_str):
        res += int(ch) * 10 ** (len(res_str) - 1 - i)

    res = res * sign
    if res < -(2**31):
        return -(2**31)
    elif res > 2**31 - 1:
        return 2**31 - 1
    else:
        return res


print(myAtoi("+42"))
print(myAtoi("-42"))
print(myAtoi(" -42"))
print(myAtoi(" --42"))
print(myAtoi(" +-42"))
print(myAtoi("word 43"))
print(myAtoi("43 word"))
print(myAtoi("  +  413"))
print(myAtoi("-91283472332"))
