from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):
    def create_expression_tree_helper(prefix_exp, start_pos):
        if isinstance(prefix_exp[start_pos], int):
            subtree_root = LinkedBinaryTree.Node(prefix_exp[start_pos])
            return (LinkedBinaryTree(subtree_root), 1)

        else:
            left = create_expression_tree_helper(prefix_exp, start_pos + 1)
            right = create_expression_tree_helper(prefix_exp, start_pos + left[1] + 1)
            subtree_root = LinkedBinaryTree.Node(prefix_exp[start_pos], left[0].root, right[0].root)
            subtree = LinkedBinaryTree(subtree_root)
            return (subtree, subtree.size)

    prefix_exp = prefix_exp_str.split(' ')
    for index in range(len(prefix_exp)):
        if prefix_exp[index] not in '+-*/':
            prefix_exp[index] = int(prefix_exp[index])

    return create_expression_tree_helper(prefix_exp, 0)[0]

def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    postfix = []
    for node in tree.postorder():
        postfix.append(str(node.data))
    postfix_exp_str = ' '.join(postfix)
    return postfix_exp_str

#print(prefix_to_postfix('* 2 + - 15 6 4'))
