class BinaryTree:

    def __init__(self, root_value):
        self.key = root_value
        self.left = None
        self.right = None

    def insert_left(self, new_node):

        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            node = BinaryTree(new_node)
            node.left = self.left
            self.left = node

    def insert_right(self, new_node):

        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            node = BinaryTree(new_node)
            node.right = self.right
            self.right = node

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.right

    def get_root_value(self):
        return self.key


tree = BinaryTree('a')
print(tree.get_root_value())

