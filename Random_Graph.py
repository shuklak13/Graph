from ModifiedGraph import Graph
from random import randrange, choice

min_edges = lambda V: V-1
max_edges = lambda V, directed: V*(V-1) if directed else V*(V-1)/2

def random_graph(min_nodes = 3, max_nodes = 6, weighted = True, max_wgt = 9, directed = True):
    V = randrange(min_nodes, max_nodes+1)
    E = randrange(min_edges(V), max_edges(V, directed))
    G = Graph(range(V), weighted, directed)
    for edge in range(E):
        G.add_edge(*random_edge(G, weighted, max_wgt))
    return G

def random_edge(G, weighted, max_wgt):
    s, t = random_node(G), random_node(G)
    while G.get_edge(s, t) or s is t:
        s, t = random_node(G), random_node(G)
    v = randrange(max_wgt+1)
    return (s, t, v) if weighted else (s, t)

def random_node(G):
    return choice(list(G.edges.keys()))

if __name__ == "__main__":
    print("\nWeighted Directed Graph:")
    print(random_graph(weighted = True, directed = True))

    print("\nWeighted Undirected Graph:")
    print(random_graph(weighted = True, directed = False))

    print("\nUnweighted Directed Graph:")
    print(random_graph(weighted = False, directed = True))
    
    print("\nUnweighted Undirected Graph:")
    print(random_graph(weighted = False, directed = False))