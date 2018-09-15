# weighted directed graph
class Graph:
    def __init__(self, nodes):
        self.edges = {node: {} for node in nodes}
    
    def add_edge(self, s, t, wgt):
        self.edges[s][t] = wgt

    def get_edge(self, s, t):
        return self.edges[s].get(t, None)

    def get_nbrs(self, s):
        return self.edges[s].keys()

    def __str__(self):
        return str(self.edges)