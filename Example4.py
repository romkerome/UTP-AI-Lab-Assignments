from collections import deque

# First, we need the Node class definition to make the tree
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def bfs_tree(root):
    if not root:
        return []
    
    # Initialize the queue with the root node
    queue = deque([root])
    result = []
    
    while queue:
        # Standard BFS: Pop from the left (First-In, First-Out)
        node = queue.popleft()
        result.append(node.val)
        
        # Add children to the queue to be processed in the next 'layer'
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result

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
print("Level Order Traversal:", bfs_tree(root)) 
# Output: [1, 2, 3, 4, 5]