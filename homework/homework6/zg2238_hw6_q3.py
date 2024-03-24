from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self, orig_str):
        self.lst = DoublyLinkedList()
        index = 0
        for i in range(len(orig_str)-1):
            if orig_str[i] != orig_str[i+1]:
                self.lst.add_last((orig_str[i],i+1-index))
                index = i+1
        if len(orig_str) >= 2:
            if orig_str[-1] == orig_str[-2]:
                self.lst.add_last((orig_str[-1],len(orig_str)-index))
            else:
                self.lst.add_last((orig_str[-2],len(orig_str)-index-1))
                self.lst.add_last((orig_str[-1],1))
        elif len(orig_str) == 1:
            self.lst.add_last((orig_str[0], 1))

    def __add__(self, other):
        concat = CompactString('')
        node = self.lst.header.next
        while node.data is not None:
            concat.lst.add_last(node.data)
            node = node.next
        if len(self.lst) != 0 and len(other.lst) != 0:
            if self.lst.trailer.prev.data[0] == other.lst.header.next.data[0]:
                concat.lst.trailer.prev.data = (self.lst.trailer.prev.data[0], self.lst.trailer.prev.data[1] + other.lst.header.next.data[1])
                node = other.lst.header.next.next
        else:
            node = other.lst.header.next
        while node.data is not None:
            concat.lst.add_last(node.data)
            node = node.next
        return concat

    def __lt__(self, other):
        node1 = self.lst.header.next
        node2 = other.lst.header.next
        while node1.data is not None and node2.data is not None:
            if node1.data[0] < node2.data[0]:
                return True
            elif node1.data[0] > node2.data[0]:
                return False
            else:
                if node1.data[1] < node2.data[1] and node1.next.data is not None:
                    if node1.next.data[0] < node2.data[0]:
                        return True
                if node1.data[1] > node2.data[1] and node2.next.data is not None:
                    if node1.data[0] < node2.next.data[0]:
                        return True
                if node1.data[1] == node2.data[1] or node1.next.data is None or node2.next.data is None:
                    node1 = node1.next
                    node2 = node2.next
                else:
                    return False
        if self.lst.trailer.prev.data is not None and other.lst.trailer.prev.data is not None:
            if self.lst.trailer.prev.data[1] < other.lst.trailer.prev.data[1]:
                return True
        elif self.lst.trailer.prev.data is None and self.lst.trailer.prev.data is not None:
            return True
        return False


    def __le__(self, other):
        if self < other:
            return True
        node1 = self.lst.header.next
        node2 = other.lst.header.next
        while node1.data is not None and node2.data is not None:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next
        if self.lst.trailer.prev.data is not None and other.lst.trailer.prev.data is not None:
            if self.lst.trailer.prev.data[1] == other.lst.trailer.prev.data[1]:
                return True
        elif self.lst.trailer.prev.data is None and self.lst.trailer.prev.data is not None:
            return True
        return False

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __repr__(self):
        return ''.join([elem[0] * elem[1] for elem in self.lst])


