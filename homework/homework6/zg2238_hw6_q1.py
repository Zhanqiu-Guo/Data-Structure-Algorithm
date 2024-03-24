from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, elem):
        self.data.add_last(elem)

    def dequeue(self):
        if self.data.is_empty() == True:
            raise Exception("Queue is empty")
        return self.data.delete_first()

    def first(self):
        if self.data.is_empty():
            raise Exception("Queue is empty")
        first = self.data.header.next.data
        return first
