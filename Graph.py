# weighted directed graph
class Graph:
    def __init__(self, nodes):
        self.edges = {node: {} for node in nodes}
    
    def add_edge(self, s, t, wgt):
        self.edges[s][t] = wgt

    def get_edge(self, s, t):
        return self.edges[s].get(t, None)

    def nodes(self):
        return self.edges.keys()

    def nbrs(self, s):
        return self.edges[s].keys()

    def __getitem__(self, s):
        return self.edges[s]

    def __len__(self):
        return len(self.edges)

    def __iter__(self):
        return self.edges.__iter__()

    def __str__(self):
        return str(self.edges)