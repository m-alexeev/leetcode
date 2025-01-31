def calculate(s: str) -> int:
    # parse
    parsed_s = []
    cur_num = ""
    for c in s:
        if c.isdigit():
            cur_num += c
        elif c in "+-*/ ":
            if len(cur_num):
                parsed_s.append(int(cur_num))
                cur_num = ""
            if c != " ":
                parsed_s.append(c)
    if len(cur_num):
        parsed_s.append(int(cur_num))
    print(parsed_s)

    stack = parsed_s
    # calculate
    res = 0

    while len(stack) > 1:
        cur = stack.pop()
        op = stack.pop()
        if op == "*":
            expr_res = stack.pop() * cur
            res += expr_res
            stack.append(expr_res)
        elif op == "/":
            expr_res = stack.pop() // cur
            res += expr_res
            stack.append(expr_res)
        elif op == "+":
            if len(stack) <= 2:
                expr_res = stack.pop() + cur
                res += expr_res
                stack.append(expr_res)
            else:
                if stack[-2] in "+-":
                    expr_res = stack.pop() + cur
                    res += expr_res
                    stack.append(expr_res)
                else:
                    stack = [cur, op] + stack

        elif op == "-":
            if len(stack) <= 2:
                expr_res = stack.pop() - cur
                res += expr_res
                stack.append(expr_res)
            else:
                if stack[-2] in "+-":
                    expr_res = stack.pop() + cur
                    res += expr_res
                    stack.append(expr_res)
                else:
                    stack = [-cur, "+"] + stack

    return stack[0]


print(calculate(s="3*2-2"))
print(calculate(s=" 3/2 "))
print(calculate(s=" 3+5 / 2 "))
