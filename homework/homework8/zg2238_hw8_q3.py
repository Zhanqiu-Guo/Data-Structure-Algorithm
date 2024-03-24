from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    if len(prefix_lst) == 0:
        return bst
    bst.insert(prefix_lst[0])
    cursor = ramify = bst.root
    for i in range(1, len(prefix_lst)):
        cursor, ramify = helper(prefix_lst[i],bst,cursor,ramify)
    return bst

def helper(key, bst, last_node, last_ramify):
    item = BinarySearchTreeMap.Item(key, None)
    new_node = BinarySearchTreeMap.Node(item)
    if key<last_node.item.key:
        last_node.left = new_node
        new_node.parent = last_node
        if last_node.parent is not None and last_node.item.key>last_node.parent.item.key:
            last_ramify = last_node
    else:
        if key > last_ramify.item.key:
            last_node = last_ramify
        while key>last_node.item.key and (last_node is not bst.root) and last_node.parent.item.key>last_node.item.key:
            last_node = last_node.parent
        if key<last_node.item.key:
            last_node = last_node.left
        last_node.right = new_node
        new_node.parent = last_node
        if last_node.parent is not None and last_node.item.key<last_node.parent.item.key:
            last_ramify = last_node
        if last_node is bst.root:
            last_ramify = bst.root
    return (new_node, last_ramify)

'''bst = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
for i in bst:
    print(i)
'''


