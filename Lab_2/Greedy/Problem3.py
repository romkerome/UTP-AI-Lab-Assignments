import heapq

graph = {
    'S': ['A', 'B'],
    'A': ['C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': ['G'],
    'G': []
}

heuristic = {
    'S': 7, 'A': 6, 'B': 2, 'C': 1, 'D': 4, 'E': 2, 'G': 0
}

def greedy_bfs(graph, heuristic, start, goal):
    # pq stores tuples of (heuristic_value, current_node)
    # Greedy BFS prioritizes based ONLY on the heuristic estimate
    pq = [(heuristic[start], start)]
    
    # visited keeps track of nodes we've already processed
    visited = {start}
    
    # parent stores {child: parent} to reconstruct the path later
    parent = {start: None}

    while pq:
        # Always pop the node that "looks" closest to the goal
        _, current_node = heapq.heappop(pq)

        if current_node == goal:
            # Reconstruct the path by backtracking
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1] # Reverse to get S -> G

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                
                # Push neighbor with its heuristic value as priority
                h_val = heuristic.get(neighbor, float('inf'))
                heapq.heappush(pq, (h_val, neighbor))

    return None

# Execution
print(f"Greedy Path: {greedy_bfs(graph, heuristic, 'S', 'G')}")