from LinkedBinaryTree import LinkedBinaryTree

def is_height_balanced(bin_tree):
    def height(root):
        if root is None:
            return (True, 0)
        else:
            left = height(root.left)
            right = height(root.right)
            if left[1] - right[1] >= 2 or left[1] - right[1] <= -2:
                flag = False
            else:
                flag = left[0] and right[0]
            return (flag, max(left[1], right[1])+1)
    return height(bin_tree.root)[0]

'''
root = LinkedBinaryTree.Node(3)
tree = LinkedBinaryTree(root)
root.left = LinkedBinaryTree.Node(2)
root.right = LinkedBinaryTree.Node(7)
root.left.left = LinkedBinaryTree.Node(9)
root.right.left = LinkedBinaryTree.Node(8)
root.right.right = LinkedBinaryTree.Node(4)
root.left.left.right = LinkedBinaryTree.Node(1)
root.left.left.left = LinkedBinaryTree.Node(5)
print(is_height_balanced(tree))
'''
