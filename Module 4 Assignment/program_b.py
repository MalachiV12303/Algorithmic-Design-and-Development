from collections import defaultdict
from graph import Graph

#Bellman Ford Algorithm
def BellmanFord(self, src):
    V=len(self.get_nodes())
    dist = [float("Inf")] * V
    dist[src] = 0
    for i in range(V - 1):
        for u in self.graph:
            if dist[u] != float("Inf") and dist[u] + u < dist[u]:
                dist[u] = dist[u] + u
        for u in self.graph:
            if dist[u] != float("Inf") and dist[u] + u < dist[u]:
                print("Negative weight cycle")
    return

nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
init_graph = {}
for node in nodes:
    init_graph[node] = {}
init_graph["A"]["B"] = 22
init_graph["A"]["C"] = 9
init_graph["A"]["D"] = 12
init_graph["B"]["C"] = 35
init_graph["B"]["F"] = 36
init_graph["B"]["H"] = 34
init_graph["C"]["F"] = 42
init_graph["C"]["E"] = 65
init_graph["C"]["D"] = 4
init_graph["F"]["H"] = 24
init_graph["F"]["G"] = 39
init_graph["F"]["E"] = 18
init_graph["E"]["G"] = 23
init_graph["E"]["D"] = 33
init_graph["D"]["I"] = 30
init_graph["G"]["I"] = 21
init_graph["G"]["H"] = 25
init_graph["H"]["I"] = 19

programbgraph = Graph(nodes, init_graph)
BellmanFord(programbgraph, 0)
