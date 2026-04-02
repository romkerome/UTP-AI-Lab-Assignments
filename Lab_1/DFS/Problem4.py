class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def dfs_preorder(node):
    if not node:
        return []
    return [node.val] + dfs_preorder(node.left) + dfs_preorder(node.right)

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(dfs_preorder(root))  # Output: [1, 2, 4, 5, 3, 6, 7]