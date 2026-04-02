import heapq

def astar_graph(graph, heuristic, start, goal):
    # pq stores: (f_score, g_score, path_list)
    # f_score = g_score + heuristic
    pq = [(heuristic[start], 0, [start])]
    visited = set()
    
    while pq:
        # Pop the path with the lowest estimated total cost (f_score)
        f_score, g_score, path = heapq.heappop(pq)
        node = path[-1]
        
        # Goal Check
        if node == goal:
            return path, g_score
            
        if node not in visited:
            visited.add(node)
            
            # Using .get() prevents a KeyError if a node has no neighbors
            for neighbor, cost in graph.get(node, []):
                if neighbor not in visited:
                    new_g = g_score + cost
                    # Calculate priority: actual cost so far + estimate to goal
                    new_f = new_g + heuristic.get(neighbor, 0)
                    
                    heapq.heappush(pq, (new_f, new_g, path + [neighbor]))
                    
    return None

# --- Example Usage ---
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('G', 12)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 10, 'B': 8, 'C': 2, 'D': 1, 'G': 0
}

path, total_cost = astar_graph(graph, heuristic, 'A', 'G')
print(f"Path: {path}\nTotal Cost: {total_cost}")