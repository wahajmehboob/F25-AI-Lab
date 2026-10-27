#task 1
#from collections import deque

#graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

#def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = []
    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path, visited
        for child in graph[node]:
            if child not in visited:
                queue.append((child, path + [child]))
    return None, visited

#def dfs(start, goal):
    stack = [(start, [start])]
    visited = []
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path, visited
        for child in reversed(graph[node]):
            if child not in visited:
                stack.append((child, path + [child]))
    return None, visited

#print("BFS:", bfs('A', 'G'))
#print("DFS:", dfs('A', 'G'))

##task 2
def dls(node, goal, limit, path=None):
    if path is None:
        path = [node]

    if node == goal:
        return "FOUND", path

    if limit == 0:
        return ("CUTOFF", None) if graph[node] else ("FAILURE", None)

    cutoff = False

    for child in graph[node]:
        if child not in path:
            status, result = dls(child, goal, limit - 1, path + [child])

            if status == "FOUND":
                return status, result
            if status == "CUTOFF":
                cutoff = True

    return ("CUTOFF", None) if cutoff else ("FAILURE", None)


def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        status, path = dls(start, goal, depth)
        print("Limit:", depth, "| Status:", status, "| Path:", path)
        if status == "FOUND":
            return path
        if status == "FAILURE":
            return None
    return None


print("DLS:")
for limit in range(1, 5):
    print("Limit:", limit, "->", dls('A', 'G', limit))

print("\nIDDFS:")
for maximum in range(1, 5):
    print("\nMaximum depth:", maximum)
    iddfs('A', 'G', maximum)

    ##task 3
    import heapq

weighted_graph = {
    'A': [('B', 1), ('C', 2), ('G', 10)],
    'B': [('D', 2), ('E', 2)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = []
    
    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            return path, cost, visited

        for child, weight in weighted_graph[node]:
            if child not in visited:
                heapq.heappush(
                    pq, (cost + weight, child, path + [child])
                )

    return None, float('inf'), visited


def bfs_weighted(start, goal):
    from collections import deque

    graph2 = {
        node: [child for child, weight in edges]
        for node, edges in weighted_graph.items()
    }

    queue = deque([(start, [start])])
    visited = []

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            cost = sum(
                next(w for n, w in weighted_graph[a] if n == b)
                for a, b in zip(path, path[1:])
            )
            return path, cost, visited

        for child in graph2[node]:
            if child not in visited:
                queue.append((child, path + [child]))

    return None, float('inf'), visited


print("UCS:", ucs('A', 'G'))
print("BFS:", bfs_weighted('A', 'G'))