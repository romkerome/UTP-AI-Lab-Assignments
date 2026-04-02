import heapq

# Heuristic: number of letters different from the goal
def h(word, goal):
    return sum(1 for a, b in zip(word, goal) if a != b)

def greedy_word_ladder(words, start, goal):
    # Priority Queue stores: (heuristic_value, current_word)
    pq = [(h(start, goal), start)]
    
    # parent stores {current_word: previous_word} 
    # This also acts as our 'visited' tracker
    parent = {start: None}

    while pq:
        # Pop the word that "looks" closest to the goal based on the heuristic
        _, current = heapq.heappop(pq)

        if current == goal:
            # Reconstruct the path by backtracking from goal to start
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1] # Reverse to get start -> goal
        
        for neighbor in words.get(current, []):
            if neighbor not in parent:
                parent[neighbor] = current
                priority = h(neighbor, goal)
                heapq.heappush(pq, (priority, neighbor))

    return None

# Word graph
words = {
    'hit': ['hot'],
    'hot': ['dot', 'lot'],
    'dot': ['dog'],
    'lot': ['log'],
    'dog': ['cog'],
    'log': ['cog'],
    'cog': []
}

start = 'hit'
goal = 'cog'

# Execution
path = greedy_word_ladder(words, start, goal)
print("Path:", path)