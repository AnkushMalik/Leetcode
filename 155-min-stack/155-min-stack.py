class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        minE = min(self.stk[-1][1], val) if self.stk else val
        self.stk.append([val, minE])

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]