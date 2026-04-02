import heapq

def heuristic(a, b):
    # Manhattan distance: |x1 - x2| + |y1 - y2|
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    
    # Priority Queue stores: (heuristic_estimate, path_list)
    pq = [(heuristic(start, goal), [start])]
    
    while pq:
        # Pop the path with the smallest heuristic value (closest to goal)
        _, path = heapq.heappop(pq)
        x, y = path[-1]
        
        # Check if we reached the goal
        if (x, y) == goal:
            return path
            
        if (x, y) not in visited:
            visited.add((x, y))
            
            # Explore neighbors: Up, Down, Left, Right
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                
                # Bounds check, wall check (grid[nx][ny] == 0), and visited check
                if 0 <= nx < rows and 0 <= ny < cols and \
                   grid[nx][ny] == 0 and (nx, ny) not in visited:
                    
                    new_path = path + [(nx, ny)]
                    heapq.heappush(pq, (heuristic((nx, ny), goal), new_path))
                    
    return None

# --- Example Usage ---
grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_node = (0, 0)
goal_node = (4, 4)

result = greedy_bfs(grid, start_node, goal_node)
print("Greedy BFS Path:", result)