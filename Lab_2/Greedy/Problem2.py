import heapq

maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]]

def heuristic(a, b):
    # Manhattan distance: |x1 - x2| + |y1 - y2|
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    
    # Priority Queue stores: (heuristic_estimate, current_coordinate)
    pq = [(heuristic(start, goal), start)]
    
    # parent dictionary stores {child_coord: parent_coord}
    # This also serves as our 'visited' tracker
    parent = {start: None}

    while pq:
        # Pop the coordinate that 'looks' closest to the goal
        _, (x, y) = heapq.heappop(pq)

        if (x, y) == goal:
            # Reconstruct path by walking backwards from goal to start
            path = []
            curr = goal
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            return path[::-1] # Reverse to get Start -> Goal

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            # Bounds check, wall check, and visited check
            if 0 <= nx < rows and 0 <= ny < cols and \
               maze[nx][ny] == 0 and (nx, ny) not in parent:
                
                parent[(nx, ny)] = (x, y)
                h_val = heuristic((nx, ny), goal)
                heapq.heappush(pq, (h_val, (nx, ny)))
                
    return None

# Maintaining your exact input and call style
print(greedy_maze(maze, (0, 0), (0, 4)))