class myStack:
    def __init__(self, n):
        self.stack = []
        self.top = 0
        self.n = n

    def isEmpty(self):
        return self.top == 0

    def isFull(self):
        return self.top == self.n

    def push(self, x):
        if self.isFull():
            return -1
        self.stack.append(x)
        self.top += 1

    def pop(self):
        if self.isEmpty():
            return -1
        self.top -= 1
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[self.top - 1]
