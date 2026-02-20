#!/usr/bin/env python3
"""
Neinformuotos Paieškos Algoritmų Palyginimas
DFS (Depth First Search) vs BFS (Breadth First Search)
"""

import networkx as nx
import time
from collections import deque
import sys

# Užtikriname, kad išvestis rodoma iškart
sys.stdout.reconfigure(line_buffering=True)

print("="*70)
print("           NEINFORMUOTOS PAIEŠKOS ALGORITMŲ PALYGINIMAS")
print("                DFS vs BFS")
print("="*70)
print()

# 1. Sukuriame paprastą grafą
print("📊 Kuriamas grafas...")
G = nx.erdos_renyi_graph(25, 0.2, seed=42)
while not nx.is_connected(G):
    G = nx.erdos_renyi_graph(25, 0.25, seed=42)

print(f"✓ Grafas sukurtas: {G.number_of_nodes()} viršūnės, {G.number_of_edges()} briaunos")
print()

# 2. DFS algoritmas
def dfs(graph, start, goal):
    start_time = time.time()
    visited = set()
    visited_order = []
    parent = {start: None}
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            visited_order.append(node)
            
            if node == goal:
                path = []
                current = goal
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return path, visited_order, time.time() - start_time
            
            neighbors = sorted(list(graph.neighbors(node)), reverse=True)
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in parent:
                    parent[neighbor] = node
                    stack.append(neighbor)
    
    return [], visited_order, time.time() - start_time

# 3. BFS algoritmas
def bfs(graph, start, goal):
    start_time = time.time()
    visited = set([start])
    visited_order = []
    parent = {start: None}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        visited_order.append(node)
        
        if node == goal:
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, visited_order, time.time() - start_time
        
        for neighbor in sorted(graph.neighbors(node)):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    
    return [], visited_order, time.time() - start_time

# 4. Vykdome testus
start, goal = 0, 24

print("🔍 Vykdomas DFS (Depth First Search)...")
dfs_path, dfs_visited, dfs_time = dfs(G, start, goal)
print(f"   Kelias: {' -> '.join(map(str, dfs_path[:10]))}{'...' if len(dfs_path) > 10 else ''}")
print(f"   Kelio ilgis: {len(dfs_path)} viršūnės")
print(f"   Aplankyta: {len(dfs_visited)} viršūnių")
print(f"   Laikas: {dfs_time*1000:.4f} ms")
print()

print("🔍 Vykdomas BFS (Breadth First Search)...")
bfs_path, bfs_visited, bfs_time = bfs(G, start, goal)
print(f"   Kelias: {' -> '.join(map(str, bfs_path[:10]))}{'...' if len(bfs_path) > 10 else ''}")
print(f"   Kelio ilgis: {len(bfs_path)} viršūnės")
print(f"   Aplankyta: {len(bfs_visited)} viršūnių")
print(f"   Laikas: {bfs_time*1000:.4f} ms")
print()

# 5. Palyginimas
print("="*70)
print("                         PALYGINIMAS")
print("="*70)
print(f"{'Metrika':<25} | {'DFS':<15} | {'BFS':<15}")
print("-"*70)
print(f"{'Kelio ilgis':<25} | {len(dfs_path):<15} | {len(bfs_path):<15}")
print(f"{'Aplankyta viršūnių':<25} | {len(dfs_visited):<15} | {len(bfs_visited):<15}")
print(f"{'Laikas (ms)':<25} | {dfs_time*1000:<15.4f} | {bfs_time*1000:<15.4f}")
print("="*70)
print()

# 6. Išvados
if len(bfs_path) < len(dfs_path):
    print(f"✓ BFS rado TRUMPESNĮ kelią: {len(bfs_path)} vs {len(dfs_path)} viršūnių")
elif len(bfs_path) > len(dfs_path):
    print(f"✓ DFS rado TRUMPESNĮ kelią: {len(dfs_path)} vs {len(bfs_path)} viršūnių")
else:
    print(f"✓ Abu algoritmai rado VIENODO ilgio kelią: {len(bfs_path)} viršūnių")

if len(dfs_visited) < len(bfs_visited):
    print(f"✓ DFS aplankė MAŽIAU viršūnių: {len(dfs_visited)} vs {len(bfs_visited)}")
else:
    print(f"✓ BFS aplankė MAŽIAU viršūnių: {len(bfs_visited)} vs {len(dfs_visited)}")

print()
print("="*70)
print("                      BENDROS IŠVADOS")
print("="*70)
print("""
BFS (Breadth First Search):
  ✓ Garantuoja TRUMPIAUSIĄ kelią
  ✓ Sistemingas tyrimas
  ✗ Naudoja daugiau atminties

DFS (Depth First Search):
  ✓ Mažiau atminties
  ✓ Greitas gilių sprendimų paieškai
  ✗ Negarantuoja trumpiausio kelio
""")
print("="*70)
print("✅ PROGRAMA BAIGTA SĖKMINGAI!")
print("="*70)
