class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def height(self, node):
        if node is None:
            return 0
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)

        return 1+max(leftHeight, rightHeight)


tree = BinaryTree(2)
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(5)
tree.root.left.right = Node(6)
tree.root.left.left.left = Node(9)
tree.root.right.left = Node(7)
tree.root.right.right = Node(8)
tree.root.right.left.left = Node(1)
tree.root.right.left.right = Node(2)
tree.root.right.right.right = Node(8)

print(tree.height(tree.root))
