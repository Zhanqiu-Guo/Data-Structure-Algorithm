class BinarySearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if self.left is not None:
                count += 1
            if self.right is not None:
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def find_node(self, key):
        curr = self.root
        while curr is not None:
            if curr.item.key == key:
                return curr  # found it!
            elif curr.item.key > key:
                curr = curr.left
            else:
                curr = curr.right
        return None  # key is not in the tree!

    def __getitem__(self, key):
        node = self.find_node(key)
        if node is None:
            raise KeyError(str(key) + " not found!")
        else:
            return node.item.value

    def insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)

        if self.is_empty():
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            curr = parent
            while curr is not None:  # find the node to insert onto
                parent = curr
                if key < curr.item.key:
                    curr = curr.left
                else:
                    curr = curr.right
            if key < parent.item.key:  # determine if the new child should a left or right
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent  # update the new node
            self.size += 1  # update the size

    def __setitem__(self, key, value):
        node = self.find_node(key)
        if node is None:
            # time to insert this key
            self.insert(key, value)
        else:
            node.item.value = value

    def inorder(self):
        def subtree_inorder(root):
            if root is not None:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def __iter__(self):
        for node in self.inorder():
            yield node.item.key
