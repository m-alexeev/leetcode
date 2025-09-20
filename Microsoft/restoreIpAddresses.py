from re import L
from typing import List


def restoreIpAddresses(s: str) -> List[str]:
    res = []
    N = len(s)
    if N < 3:
        return []

    def restore(ip, l, dots):
        if dots == 0:
            # last byte
            if len(s[l:]) > 1 and s[l:][0] == "0":
                return
            if int(s[l:]) <= 255:
                res.append(".".join(ip + [s[l:]]))
        else:
            for i in range(3):
                # try adding a dot at each digit
                if l + i + 1 < N:
                    v = s[l : l + i + 1]
                    if len(v) > 1 and v[0] == "0":
                        continue
                    if int(v) <= 255:
                        restore(ip + [v], l + i + 1, dots - 1)

    restore([], 0, 3)
    return res


print(restoreIpAddresses("0000"))
print(restoreIpAddresses("25525511135"))
print(restoreIpAddresses("101023"))
