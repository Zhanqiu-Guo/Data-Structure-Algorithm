from LinkedBinaryTree import LinkedBinaryTree

def min_and_max(bin_tree):
    if bin_tree.size == 0:
        raise Exception('Tree is empty')
    def subtree_min_and_max(root):
        if root.left:
            left = subtree_min_and_max(root.left)
            if root.right:
                right = subtree_min_and_max(root.right)
                minimum = min(left[0],right[0], root.data)
                maximum = max(left[1],right[1], root.data)
            else:
                minimum = min(left[0], root.data)
                maximum = max(left[1], root.data)
        else:
            return (root.data, root.data)
        return (minimum,maximum)
    return subtree_min_and_max(bin_tree.root)

'''
root = LinkedBinaryTree.Node(3)
tree = LinkedBinaryTree(root)
root.left = LinkedBinaryTree.Node(2)
root.right = LinkedBinaryTree.Node(7)
root.left.left = LinkedBinaryTree.Node(9)
root.left.left.left = LinkedBinaryTree.Node(5)
root.left.left.right = LinkedBinaryTree.Node(1)
root.right.left = LinkedBinaryTree.Node(8)
root.right.right = LinkedBinaryTree.Node(4)
print(min_and_max(tree))
'''
