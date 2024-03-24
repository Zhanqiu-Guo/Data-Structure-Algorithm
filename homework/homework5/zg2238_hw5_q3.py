from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.queue = ArrayDeque()
        self.stack.push(self.queue)
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def push(self, val):
        self.queue.enqueue_last(val)
        self.n += 1
        if self.n < 2 * len(self.queue):
            self.stack.pop()
            temp = self.queue.dequeue_first()
            self.stack.push(temp)
            self.stack.push(self.queue)


    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.queue.last()

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        val = self.queue.dequeue_last()
        self.n -= 1
        if self.n - len(self.queue) > len(self.queue):
            self.stack.pop()
            self.queue.enqueue_first(self.stack.pop())
            self.stack.push(self.queue)
        return val

    def mid_push(self, val):
        self.stack.pop()
        self.stack.push(val)
        self.stack.push(self.queue)
        if (self.n+1)//2 > self.n-len(self.queue):
            self.stack.pop()
            self.queue.enqueue_first(self.stack.pop())
            self.stack.push(self.queue)
        self.n += 1
