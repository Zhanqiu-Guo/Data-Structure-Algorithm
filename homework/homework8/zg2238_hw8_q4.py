from BinarySearchTreeMap import BinarySearchTreeMap

def find_min_abs_difference(bst):
    def min_sub(root):
        left = right = None
        if root.left is None and root.right is None:
            return (None, root.item.key, root.item.key)
        if root.right is not None:
            right = min_sub(root.right)
        if root.left is not None:
            left = min_sub(root.left)
        if right is not None and left is not None:
            if left[0] is None and right[0] is None:
                diff = min(root.item.key-left[2], right[1]-root.item.key)
            elif left[0] is None:
                diff = min(right[0], root.item.key-left[2], right[1]-root.item.key)
            elif right[0] is None:
                diff = min(left[0], root.item.key-left[2], right[1]-root.item.key)
            else:
                diff = min(left[0], right[0], root.item.key-left[2], right[1]-root.item.key)
            return (diff, left[1], right[2])
        elif right is None:
            if left[0] is None:
                diff = root.item.key-left[2]
            else:
                diff = min(left[0], root.item.key-left[2])
            return (diff, left[1], root.item.key)
        elif left is None:
            if right[0] is None:
                diff = right[1]-root.item.key
            else:
                diff = min(right[0], right[1]-root.item.key)
            return (diff, root.item.key, right[2])
    return min_sub(bst.root)[0]

'''tree = BinarySearchTreeMap()
tree.insert(9)
tree.insert(7)
tree.insert(4)
tree.insert(1)
tree.insert(6)
tree.insert(20)
tree.insert(17)
tree.insert(25)
print(find_min_abs_difference(tree))'''
