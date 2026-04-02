import heapq

def astar_weighted_maze(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    # Manhattan distance: |x1 - x2| + |y1 - y2|
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Priority Queue stores: (f_score, g_score, current_pos, path)
    # f_score = g_score + h_score
    pq = [(heuristic(start, goal), 0, start, [start])]
    
    # Track the minimum cost to reach each cell
    min_costs = {start: 0}

    while pq:
        f, g, (x, y), path = heapq.heappop(pq)

        # Goal check
        if (x, y) == goal:
            return path, g

        # Explore neighbors: Up, Down, Left, Right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # Boundary check
            if 0 <= nx < rows and 0 <= ny < cols:
                # Calculate the cost to move into the neighbor
                new_g = g + grid[nx][ny]
                
                # If this is the cheapest way found to reach (nx, ny)
                if (nx, ny) not in min_costs or new_g < min_costs[(nx, ny)]:
                    min_costs[(nx, ny)] = new_g
                    f_score = new_g + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (f_score, new_g, (nx, ny), path + [(nx, ny)]))

    return None

# --- Example Usage ---
# Higher numbers represent "difficult" terrain (e.g., mud or hills)
grid = [
    [1, 3, 1],
    [2, 1, 5],
    [3, 1, 1]
]

start_pos = (0, 0)
goal_pos = (2, 2)

path, total_cost = astar_weighted_maze(grid, start_pos, goal_pos)

print(f"Optimal Path: {path}")
print(f"Total Weighted Cost: {total_cost}")