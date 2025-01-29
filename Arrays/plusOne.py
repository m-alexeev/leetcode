from typing import List


def plusOne(digits: List[int]) -> List[int]:
    carry = 0
    digits[-1] += 1
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] + carry == 10:
            carry = 1
            digits[i] = 0
        else:
            digits[i] += carry
            carry = 0

        if carry == 1 and i == 0:
            digits = [1] + digits

        if carry == 0:
            break

    return digits


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9]))
print(plusOne([9, 9, 9]))
print(plusOne([8, 9, 9]))
print(plusOne([9, 8, 9]))
