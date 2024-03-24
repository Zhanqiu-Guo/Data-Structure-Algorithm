from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.value = DoublyLinkedList()
        for digit in num_str:
            self.value.add_last(int(digit))

    def __add__(self, other):
        sum = Integer('')
        tens = 0
        node1 = self.value.trailer.prev
        node2 = other.value.trailer.prev
        while node1.data is not None and node2.data is not None:
            digit1 = node1.data
            digit2 = node2.data
            units = (digit1 + digit2 + tens)%10
            tens = (digit1 + digit2 + tens)//10
            sum.value.add_first(units)
            node1 = node1.prev
            node2 = node2.prev
        if node1.data is None:
            while node2.data is not None:
                digit = node2.data
                units = (digit + tens)%10
                tens = (digit + tens)//10
                sum.value.add_first(units)
                node2 = node2.prev
        elif node2.data is None:
            while node1.data is not None:
                digit = node1.data
                units = (digit + tens)%10
                tens = (digit + tens)//10
                sum.value.add_first(units)
                node1 = node1.prev
        sum.value.add_first(tens)
        node = sum.value.header.next
        while node.data == 0 and node.next.data is not None:
            node = node.next
            sum.value.delete_first()
        return sum

    def __mul__(self, other):
        def sub_product(node1, node2, cursor):
            sub_product = Integer('')
            tens = 0
            digit2 = node2.data
            for i in range(cursor):
                sub_product.value.add_first(0)
            while node1.data is not None:
                digit1 = node1.data
                units = (digit1 * digit2 + tens)%10
                tens = (digit1 * digit2 + tens)//10
                sub_product.value.add_first(units)
                node1 = node1.prev
            sub_product.value.add_first(tens)
            return sub_product

        product = Integer('')
        node1 = self.value.trailer.prev
        node2 = other.value.trailer.prev
        cursor = 0
        while node2.data is not None:
            product = product + sub_product(node1, node2, cursor)
            node2 = node2.prev
            cursor += 1
        node = product.value.header.next
        while node.data == 0 and node.next.data is not None:
            node = node.next
            product.value.delete_first()
        return product

    def __repr__(self):
        return "".join([str(elem) for elem in self.value])


