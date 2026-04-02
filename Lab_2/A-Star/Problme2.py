grid = [
    [1, 3, 1, 2, 9],
    [7, 3, 4, 9, 2],
    [1, 7, 5, 5, 3],
    [2, 3, 2, 2, 1],
    [3, 1, 4, 2, 1]
]
import heapq

# Manhattan Distance as heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq = [(heuristic(start, goal), 0, [start])]  # (f = g + h, g, path)

    while pq:
        f, g, path = heapq.heappop(pq)
        x, y = path[-1]

        if (x, y) == goal:
            return path, g  # return final path and total cost

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # 4 directions
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                next_cost = grid[nx][ny]
                total_g = g + next_cost
                est_f = total_g + heuristic((nx, ny), goal)
                heapq.heappush(pq, (est_f, total_g, path + [(nx, ny)]))

    return None, float('inf')  # No path found

# Grid definition
grid = [
    [1, 3, 1, 2, 9],
    [7, 3, 4, 9, 2],
    [1, 7, 5, 5, 3],
    [2, 3, 2, 2, 1],
    [3, 1, 4, 2, 1]
]

start = (0, 0)
goal = (4, 4)

# Run the algorithm
path, cost = astar_grid(grid, start, goal)
print("Optimal path:", path)
print("Total cost:", cost)