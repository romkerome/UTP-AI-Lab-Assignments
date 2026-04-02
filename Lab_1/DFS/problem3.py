word_list = ["hit", "hot", "dot", "dog", "lot", "log", "cog"]

def dfs_words(current, target, word_list):
    # The stack stores: (current_word, current_path)
    # We use a list as a LIFO (Last-In, First-Out) stack
    stack = [(current, [current])]
    visited = {current}

    while stack:
        word, path = stack.pop()

        # Goal check
        if word == target:
            return path

        # Find neighbors (words with only 1 letter difference)
        for next_word in word_list:
            if next_word not in visited:
                # Check if words are "neighbors" (1-character difference)
                diff = sum(a != b for a, b in zip(word, next_word))
                
                if diff == 1:
                    visited.add(next_word)
                    # Push to stack to explore this branch deep
                    stack.append((next_word, path + [next_word]))
    
    return None

# Maintaining your exact input style, but simplifying the call
print(dfs_words("hit", "cog", word_list))