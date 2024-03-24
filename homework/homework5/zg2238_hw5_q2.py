from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        if self.is_empty():
            self.data.push((val,val))
        else:
            self.data.push((self.max(), val))

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.top()[1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        val = self.data.pop()
        return val[1]

    def max(self):
        if self.data.top()[0] >= self.data.top()[1]:
            return self.data.top()[0]
        else:
            return self.data.top()[1]
