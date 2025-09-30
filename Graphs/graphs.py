
class Graph:
    def __init__(self):
        self.graph = {}  # dictionary {node: [neighbors]}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v):
        # undirected graph
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def show(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# Example
g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('G')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('G','f')
g.add_edge('B','G')
g.show()
