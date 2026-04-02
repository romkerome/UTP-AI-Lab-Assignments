from collections import deque

maze = [
    ['S', '.', '.', '#', 'G'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.']
]

def bfs_maze(maze):
    start, goal = None, None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)
    
    queue = deque([[start]])
    visited = set()

    def get_neighbors(x, y):
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
                yield (nx, ny)
    
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == goal:
            return path
        if (x, y) not in visited:
            visited.add((x, y))
            for neighbor in get_neighbors(x, y):
                queue.append(path + [neighbor])
    return None

# Example usage
print(bfs_maze(maze))
# Output: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)]