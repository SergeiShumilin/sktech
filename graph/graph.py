import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

N = 10
for i in range(N):
    fig = plt.Figure()
    ax = fig.add_subplot()
    n_nodes = np.random.randint(2, 10)
    n_edges = np.random.randint(1, 10)
    G = nx.generators.dense_gnm_random_graph(n_nodes, n_edges)
    go = nx.algorithms.approximation.maximum_independent_set(G)
    print(go)
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, ax=ax)
    nx.draw_networkx_labels(G, pos=pos, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=list(go), node_color='red', ax=ax)
    fig.savefig(f'{i} friends.png')
