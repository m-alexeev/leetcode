def clumsyFactorial(n: int) -> int:
    cache = {}

    def factorial(n, op) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            if op == "*":
                return n * factorial(n - 1, "/")
            elif op == "/":
                return n // factorial(n - 1, "+")
            elif op == "+":
                return n + factorial(n - 1, "-")
            else:
                return n - factorial(n - 1, "*")

    return factorial(n, "*")


print(clumsyFactorial(10))
print(clumsyFactorial(4))
