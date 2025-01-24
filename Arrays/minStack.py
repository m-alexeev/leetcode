class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.minIndex = -1

    def push(self, val: int) -> None:
        if self.minIndex < 0:
            self.minIndex = 0
        else:
            if val < self.stack[self.minIndex]:
                self.minIndex = 0
            else:
                self.minIndex += 1
        self.stack.insert(0, val)

    def pop(self) -> int:
        if self.minIndex != 0:
            self.minIndex -= 1
        ret = self.stack[0]
        self.stack = self.stack[1:]
        return ret

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.stack[self.minIndex]
