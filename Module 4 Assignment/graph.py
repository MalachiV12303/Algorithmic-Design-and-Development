class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        # This makes sure each node can be traveled from either direction, if A to B is 10, B to A is also set to 10
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
        return graph
    
    def get_nodes(self):
        # Returns nodes in graph
        return self.nodes
    
    def get_out_edges(self, node):
        # Returns neighbors of a specified node
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        # Returns value of bridge between nodes
        return self.graph[node1][node2]