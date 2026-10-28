#task 1 
def minimax(tree, maximizing):
    if isinstance(tree, int):
        return tree

    values = [minimax(x, not maximizing) for x in tree]
    return max(values) if maximizing else min(values)


tree = [[3, 5], [2, 9], [12, 5]]
print("Minimax Value:", minimax(tree, True))

#task 2  
def minimax(tree, max_turn, count):
    if isinstance(tree, int):
        count[0] += 1
        return tree

    values = [minimax(x, not max_turn, count) for x in tree]
    return max(values) if max_turn else min(values)


tree = [[3, 5], [2, 9], [12, 5]]
count = [0]

print("Minimax Value:", minimax(tree, True, count))
print("Leaves Evaluated:", count[0])

#task 3
def alphabeta(tree, alpha, beta, maximizing, count):
    if isinstance(tree, int):
        count[0] += 1
        return tree

    if maximizing:
        value = float('-inf')
        for child in tree:
            value = max(value, alphabeta(
                child, alpha, beta, False, count))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else:
        value = float('inf')
        for child in tree:
            value = min(value, alphabeta(
                child, alpha, beta, True, count))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


tree = [[3, 5], [2, 9], [12, 5]]

count = [0]
print("Original Order:")
print("Value:", alphabeta(tree, float('-inf'),
      float('inf'), True, count))
print("Leaves Evaluated:", count[0])

count = [0]
tree.reverse()

print("\nReversed Order:")
print("Value:", alphabeta(tree, float('-inf'),
      float('inf'), True, count))
print("Leaves Evaluated:", count[0])