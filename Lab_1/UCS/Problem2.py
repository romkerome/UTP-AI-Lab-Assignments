import heapq

grid = [
    [1, 1, 1, 99, 1],
    [99, 99, 1, 99, 1],
    [1, 1, 1, 1, 1],
    [1, 99, 99, 99, 1],
    [1, 1, 1, 1, 1]]

def ucs_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    # Priority Queue stores: (cumulative_cost, (x, y))
    pq = [(0, start)]
    
    # visited now stores the minimum cost to reach a cell
    # This prevents re-processing cells with higher costs
    min_costs = {start: 0}
    
    # parent stores (current_cell): (previous_cell) to reconstruct the path later
    parent = {start: None}
    
    while pq:
        cost, (x, y) = heapq.heappop(pq)
        
        # Goal check
        if (x, y) == goal:
            # Reconstruct the path by backtracking from goal to start
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], cost
        
        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols:
                new_cost = cost + grid[nx][ny]
                
                # Only push to PQ if this is a cheaper path to the neighbor than found before
                if (nx, ny) not in min_costs or new_cost < min_costs[(nx, ny)]:
                    min_costs[(nx, ny)] = new_cost
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (new_cost, (nx, ny)))
                    
    return None

# Maintaining your exact input and call style
print(ucs_grid(grid, (0, 0), (0, 4)))

