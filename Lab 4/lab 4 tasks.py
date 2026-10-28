import heapq

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('C', 1), ('G', 5)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}

h = {'S': 6, 'A': 5, 'B': 4, 'C': 3, 'D': 2, 'G': 0}
pq = [(6, 0, 'S')]
visited = set()

for step in range(3):
    f, g, node = heapq.heappop(pq)

    if node in visited:
        continue

    visited.add(node)
    print("Node:", node, "g:", g, "h:", h[node], "f:", f)

    for nxt, cost in graph[node]:
        if nxt not in visited:
            ng = g + cost
            heapq.heappush(pq, (ng + h[nxt], ng, nxt))

    print("Frontier:", pq)

    #task 2
    import heapq

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('C', 1), ('G', 5)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}

h = {'S': 6, 'A': 5, 'B': 4, 'C': 3, 'D': 2, 'G': 0}


def search(astar):
    pq = [(h['S'] if astar else 0, 0, 'S', ['S'])]
    best = {'S': 0}
    expanded = []

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if g != best[node]:
            continue

        if node == 'G':
            print("Path:", path, "Cost:", g)
            print("Expanded:", expanded)
            return

        expanded.append(node)

        for nxt, cost in graph[node]:
            ng = g + cost
            if ng < best.get(nxt, float('inf')):
                best[nxt] = ng
                priority = ng + h[nxt] if astar else ng
                heapq.heappush(pq, (priority, ng, nxt, path + [nxt]))


print("A* Search:")
search(True)

print("\nUniform Cost Search:")
search(False)

#task 3
import heapq

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('C', 1), ('G', 5)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}

h = {'S': 6, 'A': 5, 'B': 4, 'C': 3, 'D': 2, 'G': 0}


def astar():
    pq = [(h['S'], 0, 'S', ['S'])]
    best = {'S': 0}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if g != best[node]:
            continue

        if node == 'G':
            print("Path:", path, "Cost:", g)
            return

        for nxt, cost in graph[node]:
            ng = g + cost
            if ng < best.get(nxt, float('inf')):
                best[nxt] = ng
                heapq.heappush(
                    pq, (ng + h[nxt], ng, nxt, path + [nxt])
                )


print("Original heuristic:")
astar()

h['C'] = 10

print("\nModified heuristic h(C) = 10:")
astar()

print("\nTrue remaining cost from C = 3")
print("Original h(C) = 3")
print("Modified h(C) = 10")