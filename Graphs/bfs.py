from collections import deque
def bfs_search(graph, start, goal):
    visited = set([start])       # keep track of visited nodes
    queue = deque([[start]])     # store paths, not just nodes

    while queue:
        path = queue.popleft()   # get first path from queue
        node = path[-1]          # current node is last in path

        if node == goal:
            return path  # 🎯 Found path to goal

        # explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  # no path found
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs_search(graph, 'A', 'E'))  # ['A', 'C', 'F']
print(bfs_search(graph, 'A', 'D'))  # ['A', 'B', 'D']
print(bfs_search(graph, 'C', 'E'))  # ['C', 'F', 'E']
