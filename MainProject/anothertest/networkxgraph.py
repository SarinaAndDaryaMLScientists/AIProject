
import networkx as nx
import networkx as nx
import matplotlib.pyplot as plt

# create the graph and set with_positions=True
a = nx.Graph()
a.add_edge(1, 2)
a.add_edge(2, 3)
a.add_edge(1, 4)
a.add_edge(2, 4)
G = nx.hexagonal_lattice_graph(m=2, n=2, periodic=False, with_positions=True, create_using=a)

# G.add_edge(0, 1)

plt.subplot(111)

# Extract the positions
pos = nx.get_node_attributes(G, 'pos')

# Pass the positions while drawing
nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
plt.show()