import heapq

def ucs(graph, start, goal):
    # pq stores tuples of (cumulative_cost, path_list)
    # The heap always pops the path with the lowest cost first
    pq = [(0, [start])]
    visited = set()
    
    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]
        
        # Goal Check
        if node == goal:
            return path, cost
        
        # Standard UCS logic: only expand the node if it's the first time 
        # reaching it (guarantees the lowest cost due to the priority queue)
        if node not in visited:
            visited.add(node)
            
            # Using .get() prevents crashes if a node has no neighbors
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    # Push the new cost and the updated path list
                    heapq.heappush(pq, (cost + weight, path + [neighbor]))
                    
    return None

# --- Example Usage ---
graph = {
    'S': [('A', 1), ('B', 5)],
    'A': [('C', 2), ('G', 10)],
    'B': [('G', 1)],
    'C': [('G', 4)],
    'G': []
}

path, total_cost = ucs(graph, 'S', 'G')
print(f"Path: {path}, Total Cost: {total_cost}")