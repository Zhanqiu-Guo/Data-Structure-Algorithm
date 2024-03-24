from ArrayQueue import ArrayQueue

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return 1 + left_count + right_count

        return subtree_count(self.root)


    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return root.data + left_sum + right_sum

        return subtree_sum(self.root)


    def height(self):
        def subtree_height(root):
            if (root.left is None and root.right is None):
                return 0
            elif (root.left is None):
                return 1 + subtree_height(root.right)
            elif (root.right is None):
                return 1 + subtree_height(root.left)
            else:
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if(self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)


    def preorder(self):
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)


    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)


    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

    def leaves_list(self):
        lst = []
        def sub_leaves(lst, root):
            if root is None:
                return
            else:
                left = sub_leaves(lst, root.left)
                right = sub_leaves(lst, root.right)
                if root.left == root.right == None:
                    lst.append(root.data)
                return lst
        return sub_leaves(lst, self.root)

    def iterative_inorder(self):
        node = self.root
        while node.left is not None:
            node = node.left
        while node is not self.root or None:
            if node.parent.left == node:
                yield node.data
                while node.right is None and node.parent.left == node:
                    node = node.parent
                    yield node.data
                node = node.right
            elif node.parent.right == node:
                if node.left is not None:
                    while node.left is not None:
                        node = node.left
                    yield node.data
                    while node.right is None:
                        node = node.parent
                        yield node.data
                    node = node.right
                elif node.left is None:
                    yield node.data
                    if node.right is None:
                        while node.parent is not self.root and node.parent.right == node:
                            node = node.parent
                        node = node.parent
                    else:
                        node = node.right



'''node41 = LinkedBinaryTree.Node(5)
node51 = LinkedBinaryTree.Node(0)
node52 = LinkedBinaryTree.Node(0)
node42 = LinkedBinaryTree.Node(1, node51, node52)
node31 = LinkedBinaryTree.Node(9, node41, node42)
node21 = LinkedBinaryTree.Node(2, node31)
node32 = LinkedBinaryTree.Node(8)
node33 = LinkedBinaryTree.Node(4)
node22 = LinkedBinaryTree.Node(7, node32, node33)
node11 = LinkedBinaryTree.Node(3, node21, node22)
tree = LinkedBinaryTree(node11)

for item in tree.iterative_inorder():
    print(item, end=' ')
print()

'''
