import heapq

def greedy_word_ladder(words, start, goal):
    # Heuristic: number of letters different from the goal word
    def h(w): 
        return sum(1 for a, b in zip(w, goal) if a != b)
    
    # Priority Queue stores: (heuristic_score, path_list)
    pq = [(h(start), [start])]
    visited = set()
    
    while pq:
        # Pop the path whose last word "looks" most like the goal
        _, path = heapq.heappop(pq)
        current = path[-1]
        
        if current == goal:
            return path
            
        if current not in visited:
            visited.add(current)
            
            # Explore neighbors from the word graph
            for neighbor in words.get(current, []):
                if neighbor not in visited:
                    # Push the new heuristic and the updated path
                    heapq.heappush(pq, (h(neighbor), path + [neighbor]))
                    
    return None

# --- Example Usage ---
word_graph = {
    'hit': ['hot'],
    'hot': ['dot', 'lot'],
    'dot': ['dog'],
    'lot': ['log'],
    'dog': ['cog'],
    'log': ['cog'],
    'cog': []
}

result = greedy_word_ladder(word_graph, 'hit', 'cog')
print("Word Ladder Path:", result)
