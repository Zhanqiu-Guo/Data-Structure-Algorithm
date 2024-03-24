from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    copy_lnk_lst = DoublyLinkedList()
    node = lnk_lst.header.next
    while node.data is not None:
        copy_lnk_lst.add_last(node.data)
        node = node.next
    return copy_lnk_lst

def deep_copy_linked_list(lnk_lst):
    copy_lnk_lst = DoublyLinkedList()
    node = lnk_lst.header.next
    while node.data is not None:
        if isinstance(node.data, DoublyLinkedList):
            copy_sub_lnk_lst = deep_copy_linked_list(node.data)
            copy_lnk_lst.add_last(copy_sub_lnk_lst)
        else:
            copy_lnk_lst.add_last(node.data)
        node = node.next
    return copy_lnk_lst
'''
lnk_lst1 = DoublyLinkedList()
elem1 = DoublyLinkedList()
elem1.add_last(1)
elem1.add_last(2)
lnk_lst1.add_last(elem1)
elem2 = 3
lnk_lst1.add_last(elem2)
lnk_lst2 = deep_copy_linked_list(lnk_lst1)
e1 = lnk_lst1.header.next
e1_1 = e1.data.header.next
e1_1.data = 10
e2 = lnk_lst2.header.next
e2_1 = e2.data.header.next
print(e2_1.data)
'''
