def validParanthesis(s: str) -> bool:
    def helper(c):
        if c == ")":
            return "("
        if c == "]":
            return "["
        if c == "}":
            return "{"

    stack = []
    for c in s:
        if c in "({[":
            stack.append(c)
        else:
            print(stack[-1], helper(c))
            if len(stack) == 0 or stack[-1] != helper(c):
                return False
            else:
                stack.pop()
    return True


print(validParanthesis("()"))
