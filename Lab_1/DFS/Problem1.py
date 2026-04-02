graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def dfs(graph, start, goal):
    # The stack stores tuples of (current_node, current_path)
    stack = [(start, [start])]
    visited = set()

    while stack:
        # LIFO: Pop the most recently added item
        node, path = stack.pop()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            
            # We reverse the neighbors to match the order of your recursive DFS
            # (Since it's a stack, the last one added is the first one out)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

print(dfs(graph, 'A', 'G'))