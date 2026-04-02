import heapq

def astar_grid(grid, start, goal):
    # Manhattan distance heuristic
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    rows, cols = len(grid), len(grid[0])
    
    # pq stores: (f_score, g_score, path_list)
    # f_score = g_score + heuristic
    pq = [(heuristic(start, goal), 0, [start])]
    visited = set()
    
    while pq:
        # Pop the node with the lowest f_score
        f_score, g_score, path = heapq.heappop(pq)
        x, y = path[-1]
        
        # Goal Check
        if (x, y) == goal:
            return path, g_score
            
        if (x, y) not in visited:
            visited.add((x, y))
            
            # Explore neighbors: Up, Down, Left, Right
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                
                # Check grid boundaries
                if 0 <= nx < rows and 0 <= ny < cols:
                    # new_g is the current path cost + the value in the grid cell
                    # (Assumes grid[nx][ny] represents the 'travel cost')
                    new_g = g_score + grid[nx][ny]
                    
                    if (nx, ny) not in visited:
                        f_score = new_g + heuristic((nx, ny), goal)
                        heapq.heappush(pq, (f_score, new_g, path + [(nx, ny)]))
                        
    return None

# --- Example Usage ---
# 1s are normal paths, 99s are expensive "mountains" or obstacles
maze = [
    [1, 1, 1, 99, 1],
    [99, 99, 1, 99, 1],
    [1, 1, 1, 1, 1],
    [1, 99, 99, 99, 1],
    [1, 1, 1, 1, 1]
]

start_pos = (0, 0)
goal_pos = (0, 4)

path, total_cost = astar_grid(maze, start_pos, goal_pos)
print(f"Path: {path}\nTotal Cost: {total_cost}")