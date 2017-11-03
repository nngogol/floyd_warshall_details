import networkx as nx
G = nx.gnm_random_graph(15,50)
resu = nx.algorithms.shortest_paths.dense.floyd_warshall(G, do_csv=True)