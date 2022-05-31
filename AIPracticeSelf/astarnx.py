import networkx as nx

G = nx.grid_graph(dim=[3, 3])
nx.set_edge_attributes(G, {e: e[1][0] * 2 for e in G.edges()}, "cost")


def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return 0

g = nx.Graph()
g.add_edge((0,0), (0,1), cost = 50)
g.add_edge((0, 0), (0, 2), cost = 100)
g.add_edge((0,0), (0, 2), cost = 20)
g.add_edge((0,0), (0, 3), cost = 200)
g.add_edge((0,2), (0,3), cost = 10)
destx = 0
desty = 3
print(nx.astar_path(g, (0, 0), (destx, desty), heuristic=dist, weight="cost"))
print(nx.dijkstra_path(g, (0, 0), (destx, desty), weight="cost"))
