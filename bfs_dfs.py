from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    
    def bfs(self, v):
        visited = set()
        queue = []
        
        visited.add(v)
        queue.append(v)
        
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Create an empty graph
graph = Graph()

# Take user input for the number of edges
num_edges = int(input("Enter the number of edges: "))

# Take user input for the edges
for _ in range(num_edges):
    u, v = input("Enter edge (u v): ").split()
    graph.add_edge(u, v)

# Perform DFS traversal
start_vertex = input("Enter the starting vertex for DFS: ")
print("DFS Traversal:")
graph.dfs(start_vertex, set())

# Perform BFS traversal
start_vertex = input("\nEnter the starting vertex for BFS: ")
print("\nBFS Traversal:")
graph.bfs(start_vertex)
