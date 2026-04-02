import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 4, 'D': 3, 'E': 2, 'F': 2, 'G': 0
}

def astar(graph, heuristic, start, goal):
    # pq stores: (f_score, g_score, current_node)
    # f = g (actual cost) + h (estimated cost)
    pq = [(heuristic[start], 0, start)]
    
    # g_scores tracks the cheapest path found to each node so far
    g_scores = {start: 0}
    
    # parent tracks {child: parent} for final path reconstruction
    parent = {start: None}

    while pq:
        f_score, g_score, current = heapq.heappop(pq)

        if current == goal:
            # Reconstruct path by walking backwards
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], g_score

        # Explore neighbors
        for neighbor, weight in graph.get(current, []):
            tentative_g_score = g_score + weight
            
            # If this path to neighbor is better than any previously found
            if tentative_g_score < g_scores.get(neighbor, float('inf')):
                parent[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic.get(neighbor, 0)
                heapq.heappush(pq, (f_score, tentative_g_score, neighbor))
                
    return None

# Maintaining your exact input and call style
print(astar(graph, heuristic, 'A', 'G'))