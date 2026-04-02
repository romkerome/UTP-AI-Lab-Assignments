def is_neighbor(w1, w2):
    return sum(a != b for a, b in zip(w1, w2)) == 1

def word_dfs(start, end, word_list, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = {start}
    
    # Base Case: Goal reached
    if start == end:
        return path

    # Recursive Step
    for next_word in word_list:
        if next_word not in visited and is_neighbor(start, next_word):
            visited.add(next_word)
            result = word_dfs(next_word, end, word_list, path + [next_word], visited)
            
            if result:
                return result
            
            # Backtracking: In some DFS variants you'd remove the word from visited here, 
            # but for a simple path search, keeping it visited prevents redundant loops.
            
    return None

# Example usage (Input remains exactly the same)
word_list = ["hit", "hot", "dot", "dog", "lot", "log", "cog"]
print(word_dfs("hit", "cog", word_list))