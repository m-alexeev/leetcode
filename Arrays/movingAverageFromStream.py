from collections import deque


class MovingAverage:

    def __init__(self, size: int) -> None:
        self.q = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum += val
        if len(self.q) == self.size:
            pop = self.q.pop()
            self.sum -= pop
        self.q.append(val)

        return self.sum / len(self.q)
