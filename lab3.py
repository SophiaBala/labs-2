class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_next(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current

    current = node
    while current.parent and current.parent.right == current:
        current = current.parent
    return current.parent


root = BinaryTree(15)
root.left = BinaryTree(17, parent=root)
root.right = BinaryTree(10, parent=root)
root.left.left = BinaryTree(9, parent=root.left)
root.left.right = BinaryTree(2, parent=root.left)
root.right.right = BinaryTree(9, parent=root.right)
root.right.right.right = BinaryTree(2, parent=root.left.right)


node = root.left.right
successor = find_next(root, node)
if next:
    print(f"The successor of node {node.value} is {successor.value}.")
else:
    print(f"The node {node.value} has no in-order successor.")
