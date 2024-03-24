from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(merged_list, node1, node2):
        if node1.data is None:
            while node2.data is not None:
                merged_list.add_last(node2.data)
                node2 = node2.next
        elif node2.data is None:
            while node1.data is not None:
                merged_list.add_last(node1.data)
                node1 = node1.next
        else:
            if node1.data <= node2.data:
                merged_list.add_last(node1.data)
                merge_sublists(merged_list, node1.next, node2)
            else:
                merged_list.add_last(node2.data)
                merge_sublists(merged_list, node1, node2.next)
        return merged_list
    return merge_sublists(DoublyLinkedList(), srt_lnk_lst1.header.next, srt_lnk_lst2.header.next)

