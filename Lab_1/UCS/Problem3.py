import heapq

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('D', 1)],
    'C': [('A', 5), ('D', 2)],
    'D': [('B', 1), ('C', 2), ('G', 3)],
    'G': []
}

def ucs(graph, start, goal):
    # pq stores (cumulative_cost, current_node)
    pq = [(0, start)]
    
    # distances stores the minimum cost found so far to reach each node
    distances = {start: 0}
    
    # parent stores the node we came from to reach the current node
    parent = {start: None}
    
    # visited keeps track of nodes whose shortest path is finalized
    visited = set()
    
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        
        if current_node == goal:
            # Reconstruct the path by backtracking through parents
            path = []
            temp = goal
            while temp is not None:
                path.append(temp)
                temp = parent[temp]
            return path[::-1], current_cost
            
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        for neighbor, weight in graph.get(current_node, []):
            new_cost = current_cost + weight
            
            # If we found a cheaper way to get to this neighbor
            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(pq, (new_cost, neighbor))
                
    return None

# Maintaining your exact input and call style
print(ucs(graph, 'A', 'G'))