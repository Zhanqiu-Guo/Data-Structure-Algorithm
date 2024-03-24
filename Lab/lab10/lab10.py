from DoublyLinkedList import DoublyLinkedList

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.add_first(e)

    def top(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.header.next.data

    def pop(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.delete_first()

class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid_node = self.header

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.add_first(e)
        if len(self) % 2 != 0:
            self.mid_node = self.mid_node.next

    def top(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.header.next.data

    def pop(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        pop_val = self.delete_first()
        if len(self) == 0:
            self.mid_node = self.mid_node.prev
        return pop_val

    def mid_push(self, e):
        ''' Adds an element, e, to the middle of the stack.'''
        if(self.is_empty()):
            raise Exception("List is empty")
        self.add_after(self.mid_node, e)
'''
class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def disconnect(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.last = None
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        new_node = DoublyLinkedList.Node(val)
        prev_node = node
        next_node = node.next
        prev_node.next = new_node
        new_node.next = next_node
        self.n += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        node_before = self.header
        return self.add_after(node.prev, val)

    def delete_node(self, node):
        data = node.data
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.n -= 1
        node.disconnect()
        return data

    def delete_first(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        cursor = self.header.next
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return '[' + " <--> ".join([str(elem) for elem in self]) + ']'
'''
def reverse_dll_by_data(dll):
    first_node = dll.header
    last_node = dll.trailer
    for i in range(len(dll)//2):
        first_node.data, last_node.data = last_node.data, first_node.data
        first_node = first_node.next
        last_node = last_node.prev

def reverse_dll_by_node(dll):
    first_node = dll.header
    last_node = dll.trailer
    for i in range(len(dll)//2):
        next_node = first_node.next
        prev_node = last_node.prev
        first_node.next, last_node.prev = last_node.prev, first_node.next
        first_node.next.prev, first_node.next.next, last_node.prev.prev, last_node.prev.next = \
            last_node.prev.prev, last_node, first_node, first_node.next.prev
        first_node = next_node
        last_node = prev_node

dll = DoublyLinkedList()
for i in range(10):
    dll.add_last(i)
reverse_dll_by_node(dll)
print(dll)
