def post_order(tree):
    if tree is not None:
        post_order(tree.left)
        post_order(tree.right)
        print(tree.get_rootValue())


def in_order(tree):
    if tree is not None:
        in_order(tree.left)
        print(tree.get_rootValue())
        in_order(tree.right)


def pre_order(tree):
    if tree is not None:
        print(tree.get_rootValue())
        pre_order(tree.left)
        pre_order(tree.right)
