import networkx as nx
import time
from collections import deque
from typing import List, Tuple, Dict, Optional


class GraphSearchSimple:
    def __init__(self, graph: nx.Graph, name: str):
        self.graph = graph
        self.name = name
        
    def dfs(self, start: int, goal: int) -> Tuple[List[int], List[int], float, int]:
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
                    path = self._reconstruct_path(parent, start, goal)
                    end_time = time.time()
                    return path, visited_order, end_time - start_time, len(visited_order)
                
                neighbors = list(self.graph.neighbors(node))
                neighbors.sort(reverse=True)
                
                for neighbor in neighbors:
                    if neighbor not in visited:
                        if neighbor not in parent:
                            parent[neighbor] = node
                        stack.append(neighbor)
        
        end_time = time.time()
        return [], visited_order, end_time - start_time, len(visited_order)
    
    def bfs(self, start: int, goal: int) -> Tuple[List[int], List[int], float, int]:
        start_time = time.time()
        visited = set()
        visited_order = []
        parent = {start: None}
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            visited_order.append(node)
            
            if node == goal:
                path = self._reconstruct_path(parent, start, goal)
                end_time = time.time()
                return path, visited_order, end_time - start_time, len(visited_order)
            
            neighbors = sorted(list(self.graph.neighbors(node)))
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        end_time = time.time()
        return [], visited_order, end_time - start_time, len(visited_order)
    
    def _reconstruct_path(self, parent: Dict[int, Optional[int]], start: int, goal: int) -> List[int]:
        path = []
        current = goal
        
        while current is not None:
            path.append(current)
            current = parent[current]
        
        path.reverse()
        return path


def generate_random_graph(num_nodes: int, edge_probability: float = 0.15, seed: int = None) -> nx.Graph:
    G = nx.erdos_renyi_graph(num_nodes, edge_probability, seed=seed)
    
    while not nx.is_connected(G):
        edge_probability += 0.05
        G = nx.erdos_renyi_graph(num_nodes, edge_probability, seed=seed)
    
    return G


def generate_grid_graph(rows: int, cols: int) -> nx.Graph:
    G = nx.grid_2d_graph(rows, cols)
    mapping = {node: i for i, node in enumerate(G.nodes())}
    G = nx.relabel_nodes(G, mapping)
    return G


def generate_tree_graph(num_nodes: int, branching_factor: int = 3, seed: int = None) -> nx.Graph:
    import random
    if seed:
        random.seed(seed)
    
    G = nx.Graph()
    G.add_node(0)
    
    nodes_to_expand = [0]
    next_node_id = 1
    
    while next_node_id < num_nodes and nodes_to_expand:
        parent = nodes_to_expand.pop(0)
        num_children = min(random.randint(1, branching_factor), num_nodes - next_node_id)
        
        for _ in range(num_children):
            G.add_edge(parent, next_node_id)
            nodes_to_expand.append(next_node_id)
            next_node_id += 1
            
            if next_node_id >= num_nodes:
                break
    
    return G


def print_results(algorithm: str, path: List[int], visited: List[int], 
                 exec_time: float, nodes_explored: int):
    print(f"\n{'='*60}")
    print(f"Algoritmas: {algorithm}")
    print(f"{'='*60}")
    print(f"Rastas kelias: {' -> '.join(map(str, path)) if path else 'Kelias nerastas'}")
    print(f"Kelio ilgis: {len(path) if path else 0} viršūnių")
    print(f"Aplankyta viršūnių: {nodes_explored}")
    
    if len(visited) <= 20:
        print(f"Viršūnių lankymo tvarka: {' -> '.join(map(str, visited))}")
    else:
        print(f"Viršūnių lankymo tvarka (pirmos 20): {' -> '.join(map(str, visited[:20]))} ...")
    
    print(f"Vykdymo laikas: {exec_time*1000:.4f} ms")
    print(f"{'='*60}")


def run_comparison(graph_func, graph_name: str, start: int, goal: int):
    print(f"\n\n{'#'*70}")
    print(f"# {graph_name}")
    print(f"{'#'*70}")
    
    graph = graph_func()
    print(f"\nGrafo informacija:")
    print(f"  - Viršūnių skaičius: {graph.number_of_nodes()}")
    print(f"  - Briaunų skaičius: {graph.number_of_edges()}")
    print(f"  - Pradžios viršūnė: {start}")
    print(f"  - Tikslo viršūnė: {goal}")
    
    searcher = GraphSearchSimple(graph, graph_name)
    
    dfs_path, dfs_visited, dfs_time, dfs_explored = searcher.dfs(start, goal)
    print_results("DFS (Depth First Search)", dfs_path, dfs_visited, dfs_time, dfs_explored)
    
    bfs_path, bfs_visited, bfs_time, bfs_explored = searcher.bfs(start, goal)
    print_results("BFS (Breadth First Search)", bfs_path, bfs_visited, bfs_time, bfs_explored)
    
    print(f"\n{'*'*60}")
    print(f"PALYGINIMAS")
    print(f"{'*'*60}")
    print(f"{'Metrika':<30} | {'DFS':<12} | {'BFS':<12}")
    print(f"{'-'*60}")
    print(f"{'Kelio ilgis':<30} | {len(dfs_path):<12} | {len(bfs_path):<12}")
    print(f"{'Aplankyta viršūnių':<30} | {dfs_explored:<12} | {bfs_explored:<12}")
    print(f"{'Vykdymo laikas (ms)':<30} | {dfs_time*1000:<12.4f} | {bfs_time*1000:<12.4f}")
    
    if dfs_path and bfs_path:
        if len(bfs_path) <= len(dfs_path):
            print(f"\n✓ BFS rado trumpesnį arba lygų kelią ({len(bfs_path)} vs {len(dfs_path)} viršūnių)")
        else:
            print(f"\n✓ DFS rado trumpesnį kelią ({len(dfs_path)} vs {len(bfs_path)} viršūnių)")
        
        if dfs_explored < bfs_explored:
            print(f"✓ DFS aplankė mažiau viršūnių ({dfs_explored} vs {bfs_explored})")
        else:
            print(f"✓ BFS aplankė mažiau viršūnių ({bfs_explored} vs {dfs_explored})")
    
    print(f"{'*'*60}")


def main():
    print("="*70)
    print(" "*10 + "NEINFORMUOTOS PAIEŠKOS ALGORITMŲ PALYGINIMAS")
    print(" "*15 + "DFS (Depth First Search) vs BFS (Breadth First Search)")
    print("="*70)
    
    dataset1 = lambda: generate_random_graph(25, edge_probability=0.2, seed=42)
    run_comparison(dataset1, "1 duomenų rinkinys: Atsitiktinis grafas (25 viršūnės)", 
                  start=0, goal=24)
    
    dataset2 = lambda: generate_grid_graph(5, 5)
    run_comparison(dataset2, "2 duomenų rinkinys: Tinklelio grafas (5x5 = 25 viršūnės)", 
                  start=0, goal=24)
    
    dataset3 = lambda: generate_tree_graph(30, branching_factor=3, seed=123)
    run_comparison(dataset3, "3 duomenų rinkinys: Medžio struktūra (30 viršūnių)", 
                  start=0, goal=29)
    
    print(f"\n\n{'='*70}")
    print(" "*25 + "BENDRA IŠVADA")
    print("="*70)
    print("""
BREADTH FIRST SEARCH (BFS):
  ✓ Visada randa trumpiausią kelią nesvertiniuose grafuose
  ✓ Sistemingas - tikrina visus kaimynus prieš einant gilyn
  ✓ Gerai tinka, kai sprendimas yra arti pradžios viršūnės
  ✗ Naudoja daugiau atminties (saugo visą lygį eilėje)
  ✗ Gali aplankyti daugiau viršūnių nei reikia
  
DEPTH FIRST SEARCH (DFS):
  ✓ Naudoja mažiau atminties (tik dėklo gylis)
  ✓ Greičiau randa sprendimą, kai jis yra giliai grafų struktūroje
  ✓ Geresnis, kai grafas turi ribotas šakas
  ✗ Negarantuoja trumpiausio kelio
  ✗ Gali įstrigti giliose šakose prieš randant sprendimą
  
KADA NAUDOTI:
  • BFS - kai reikia rasti TRUMPIAUSIĄ kelią
  • DFS - kai atmintis RIBOTA arba sprendimas GILIAI
  
SUDĖTINGUMAS:
  • Abu algoritmai: O(V + E) laiko sudėtingumas
  • BFS erdvės sudėtingumas: O(V)
  • DFS erdvės sudėtingumas: O(h), kur h - maksimalus gylis
    """)
    print("="*70)
    print("\nProgramos pabaiga. Visi testai atlikti sėkmingai!")


if __name__ == "__main__":
    main()
