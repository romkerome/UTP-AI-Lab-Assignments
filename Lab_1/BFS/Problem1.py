graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def dls(node, goal, depth, path, visited):
    """Depth-Limited Search helper function."""
    if depth == 0 and node == goal:
        return path
    if depth > 0:
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                result = dls(neighbor, goal, depth - 1, path + [neighbor], visited)
                if result is not None:
                    return result
                visited.remove(neighbor) # Backtracking
    return None

def bfs(graph, start, goal):
    """Implementing IDDFS to replace standard BFS logic."""
    # We gradually increase the allowed depth (0, 1, 2...)
    for depth in range(len(graph)):
        visited = {start}
        path = dls(start, goal, depth, [start], visited)
        if path:
            return path
    return None

# Example usage
print(bfs(graph, 'A', 'G'))