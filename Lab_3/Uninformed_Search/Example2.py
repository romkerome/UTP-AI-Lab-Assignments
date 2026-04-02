def dfs_maze(grid, x, y, path, visited, goal):
    # Base Case: If current position is the goal, return the path
    if (x, y) == goal:
        return path
    
    # Mark the current cell as visited
    visited.add((x, y))
    
    # Explore neighbors: Up, Down, Left, Right
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        
        # 1. Check grid boundaries
        # 2. Check if the cell is walkable (0)
        # 3. Check if we haven't visited this cell in the current path
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and \
           grid[nx][ny] == 0 and (nx, ny) not in visited:
            
            # Recurse with the updated path
            result = dfs_maze(grid, nx, ny, path + [(nx, ny)], visited, goal)
            
            # If a path was found in the recursion, pass it up the stack
            if result:
                return result
    
    # Optional: Backtracking. If you want to find ALL paths or 
    # if the grid allows re-entry from different branches.
    # visited.remove((x, y)) 
    
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

# We start the path with the initial node already inside it
result_path = dfs_maze(grid, start_node[0], start_node[1], [start_node], set(), goal_node)

print("DFS Path found:", result_path)