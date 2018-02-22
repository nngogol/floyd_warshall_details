import networkx as nx

#               #############################
# 1.             Choose a graph

# 		Create path-graph
# 		Создает граф-цепь на 6 вершин
# G=nx.path_graph(6)
# OR 	Create graph(v,e), where v - # vertex | e - # edges
# 		Создает граф с v вершинами и e ребрами
# G = nx.gnm_random_graph(15,50)

#         OR

# Read graph from file
# Читаем граф из файла
G = nx.read_edgelist("1.test", nodetype=int)
# Формат файла: откуда{пробел}куда
# Детали: https://networkx.github.io/documentation/networkx-1.9/reference/readwrite.edgelist.html
# 1 2
# 3 1
# 2 4
# 3 4

# Show graph
# print(G.edges)


#               #############################
# 2.               Do floyd Warshall alg
# 2.               Делаем дела :)
nx.algorithms.shortest_paths.dense.floyd_warshall(G, do_csv=True)



#               #############################
# 3. (optional)    Export graph

# export
# nx.write_edgelist(G, "test.edgelist")
