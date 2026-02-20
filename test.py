#!/usr/bin/env python3
print("Starting test...")
import networkx as nx
print("NetworkX imported")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("Matplotlib imported")

# Generate simple graph
G = nx.erdos_renyi_graph(10, 0.3)
print(f"Graph created with {G.number_of_nodes()} nodes")

# Test DFS
from collections import deque

def simple_bfs(graph, start, goal):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node == goal:
            return True
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

result = simple_bfs(G, 0, 5)
print(f"BFS result: {result}")

# Create simple visualization
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500)
plt.savefig('/mnt/d/programing/intelektika-1/test_graph.png')
print("✓ Test graph saved to test_graph.png")
print("Test completed successfully!")
