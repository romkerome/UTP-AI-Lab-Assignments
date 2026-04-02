import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 2,
    'G': 0
}

def greedy_bfs(graph, heuristic, start, goal):
    # Priority Queue stores: (heuristic_value, current_node)
    pq = [(heuristic[start], start)]
    
    # visited keeps track of nodes we have already explored
    visited = {start}
    
    # parent stores current_node: previous_node to reconstruct the path
    parent = {start: None}

    while pq:
        # Pop the node with the lowest heuristic value (closest to goal)
        _, node = heapq.heappop(pq)
        
        if node == goal:
            # Reconstruct the path by backtracking
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1] # Reverse to get start -> goal

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                # Greedy only cares about the heuristic of the next node
                h_val = heuristic.get(neighbor, float('inf'))
                heapq.heappush(pq, (h_val, neighbor))
                
    return None

# Maintaining your exact input and call style
print(greedy_bfs(graph, heuristic, 'A', 'G'))