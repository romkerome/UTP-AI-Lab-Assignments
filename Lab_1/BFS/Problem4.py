class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def depth_first_search(root):
    if not root:
        return []
    
    result = []
    # Use a list as a stack (LIFO)
    stack = [root]
    
    while stack:
        # Pop the most recently added node
        node = stack.pop()
        result.append(node.val)
        
        # Push RIGHT child first so that LEFT is processed first 
        # (Since it's a stack, the last one pushed is the first one popped)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return result

# Keeping your exact input structure
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(depth_first_search(root)) 
# Output: [1, 2, 4, 5, 3, 6, 7]
