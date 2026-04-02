from collections import deque

def bfs_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    visited.add(start)
    queue = deque([(start, [start])])
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == goal:
            return path
            
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            # Fixed the syntax and logic to ensure it runs correctly
            if 0 <= nx < rows and 0 <= ny < cols and \
               grid[nx][ny] == 0 and (nx, ny) not in visited:
                
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
                
    return None 

# Example usage to verify it works
maze_grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_pos = (0, 0)
goal_pos = (4, 4)

print(bfs_grid(maze_grid, start_pos, goal_pos))