# We need the Node class to create the tree structure
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def dfs_preorder(root):
    # Base Case: If the current node is empty, return an empty list
    if not root:
        return []
    
    # Pre-order Logic: [Root] + [Left subtree] + [Right subtree]
    return [root.val] + dfs_preorder(root.left) + dfs_preorder(root.right)

# --- Example Usage ---
# Creating a simple tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Execute and print result
print("Pre-order DFS:", dfs_preorder(root))
# Expected Output: [1, 2, 4, 5, 3]