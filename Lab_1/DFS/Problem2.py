maze = [
    ['S', '.', '.', '#', 'G'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.']]

def dfs_maze(maze, start_x, start_y):
    rows, cols = len(maze), len(maze[0])
    
    # The stack stores tuples of (current_coordinate, path_taken)
    # A list in Python acts perfectly as a LIFO stack
    stack = [((start_x, start_y), [(start_x, start_y)])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        # Goal Check
        if maze[x][y] == 'G':
            return path

        if (x, y) not in visited:
            visited.add((x, y))

            # Explore neighbors: Up, Down, Left, Right
            # We iterate in reverse if we want to prioritize 
            # the same direction as your recursive version
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy

                # Boundary and Wall check
                if 0 <= nx < rows and 0 <= ny < cols and \
                   maze[nx][ny] != '#' and (nx, ny) not in visited:
                    
                    # Push the neighbor and the updated path onto the stack
                    stack.append(((nx, ny), path + [(nx, ny)]))

    return None

# Maintaining your exact input style
start = (0, 0)
path = dfs_maze(maze, start[0], start[1])
print(path)
