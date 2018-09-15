from Graph import Graph as WeightedGraph

def Graph(nodes, weighted, directed):
    if weighted and directed:
        return WeightedGraph(nodes)
    elif not weighted and directed:
        return UnweightedGraph(nodes)
    elif weighted and not directed:
        return UndirectedGraph(nodes)
    elif not weighted and not directed:
        return UnweightedUndirectedGraph(nodes)

class UndirectedGraph(WeightedGraph):
    def add_edge(self, s, t, wgt):
        WeightedGraph.add_edge(self, s, t, wgt)
        WeightedGraph.add_edge(self, t, s, wgt)

class UnweightedGraph(WeightedGraph):
    def add_edge(self, s, t):
        WeightedGraph.add_edge(self, s, t, 1)
    def get_edge(self, s, t):
        return t in self.edges[s]

class UnweightedUndirectedGraph(UnweightedGraph, UndirectedGraph):
    def add_edge(self, s, t):
        UnweightedGraph.add_edge(self, s, t)
        UnweightedGraph.add_edge(self, t, s)