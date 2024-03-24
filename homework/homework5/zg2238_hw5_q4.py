from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.data1 = ArrayStack()
        self.data2 = ArrayStack()
        self.n = 0
        self.first_elem = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def enqueue(self, elem):
        if self.is_empty():
            self.first_elem = elem
        self.data1.push(elem)
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.data2.is_empty():
            while not self.data1.is_empty():
                self.data2.push(self.data1.pop())
        value = self.data2.pop()
        self.n -= 1
        if self.is_empty():
            self.first_elem = None
        elif self.data2.is_empty():
            while not self.data1.is_empty():
                self.data2.push(self.data1.pop())
        else:
            self.first_elem = self.data2.top()
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.first_elem













