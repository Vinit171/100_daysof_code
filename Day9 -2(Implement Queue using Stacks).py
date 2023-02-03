class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        self.ans = self.stack1.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.ans

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return (True)

        else:
            return (False)

# Your MyQueue object will be instantiated and called as such:
