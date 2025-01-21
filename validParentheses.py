def validParenthesis(s: str) -> bool:
    stack = []
    for c in s:
        if c in "({[":
            stack.append(c)
        if len(stack) == 0:
            return False
        elif c == ")":
            if stack.pop() != "(":
                return False
        elif c == "}":
            if stack.pop() != "{":
                return False
        elif c == "]":
            if stack.pop() != "[":
                return False
    if len(stack) > 0:
        return False
    return True


print(validParenthesis("()()"))
print(validParenthesis("{[}"))
print(validParenthesis("{[}]"))
print(validParenthesis("{][]}]"))
print(validParenthesis("()[]{"))
print(validParenthesis("()[]}"))
