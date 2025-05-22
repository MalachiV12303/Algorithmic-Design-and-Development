import sys
import timeit
from graph import Graph


#Program A - Algorithm
def dijkstra_algorithm(graph, start_node):
    unv_nodes = list(graph.get_nodes())
    min_path = {}
    prev_n = {}
    max_value = sys.maxsize
    for node in unv_nodes:
        min_path[node] = max_value
    min_path[start_node] = 0
    while unv_nodes:
        current_min_node = None
        for node in unv_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif min_path[node] < min_path[current_min_node]:
                current_min_node = node  
        # The code  below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_out_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = min_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < min_path[neighbor]:
                min_path[neighbor] = tentative_value
                # Update the best path to the current node
                prev_n[neighbor] = current_min_node
        # After visiting its neighbors, mark the node as "visited"
        unv_nodes.remove(current_min_node)
    return prev_n, min_path
# Prints outputs
def print_result(prev_n, min_path, start_node, target_node):
    path = []
    node = target_node
    while node != start_node:
        path.append(node)
        node = prev_n[node]
    # Add the start node manually
    path.append(start_node)
    print("Shortest path has value of {}.".format(min_path[target_node]))
    print(" -> ".join(reversed(path)))

# Creating graph, adding nodes and distances  
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
programagraph = Graph(nodes, init_graph)

# Testing Functionality using timeit
def program_a_test():
    programagraph = Graph(nodes, init_graph)
    #this line runs the algorithm, these values are used for the print function but not needed in this test function
    prev_n, min_path = dijkstra_algorithm(graph=programagraph, start_node="A")
# Outputs average time and the shortest path
print("Program A - Dijkstra’s Algorithm\nAverage Time to Locate Shortest Path Between A and I:", timeit.timeit(program_a_test, number=10000))
programagraph = Graph(nodes, init_graph)
prev_n, min_path = dijkstra_algorithm(graph=programagraph, start_node="A")
print_result(prev_n, min_path, start_node="A", target_node="I")