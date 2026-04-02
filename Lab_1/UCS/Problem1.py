import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 2)],
    'C': [('F', 5)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

def ucs(graph, start, goal):
    # pq stores (cumulative_cost, current_node)
    pq = [(0, start)]
    
    # Track the minimum cost to reach each node
    min_costs = {start: 0}
    
    # Track the parent of each node to reconstruct the path later
    parent = {start: None}
    
    while pq:
        current_cost, node = heapq.heappop(pq)
        
        # Goal check
        if node == goal:
            # Reconstruct the path by backtracking through parents
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], current_cost
        
        # If we found a more expensive path to a node we've already 
        # processed cheaply, skip it
        if current_cost > min_costs.get(node, float('inf')):
            continue
            
        for neighbor, weight in graph.get(node, []):
            new_cost = current_cost + weight
            
            # If this path to neighbor is cheaper than any previously found path
            if new_cost < min_costs.get(neighbor, float('inf')):
                min_costs[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))
                
    return None

# Maintaining your exact input and call style
print(ucs(graph, 'A', 'G'))
