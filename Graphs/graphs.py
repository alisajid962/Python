graph = {
    1: [4, 3, 2],
    2: [6, 5],
    3: [],
    4: [8, 7],
    5: [10, 9],
    6: [],
    7: [11],
    8: [],
    9: [],
    10: [],
    11: [12],
    12: []
}

visited = []

def dfs(node, graph, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, graph, visited)

dfs(1, graph, visited)
print("Modified DFS Traversal:", visited)
