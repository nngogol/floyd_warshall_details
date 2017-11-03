# floyd_warshall_details
floyd_warshall from networkX with details
# Алгоритм floyd_warshall на графах
## ЗАЧЕМ?
##### Прост)
## КАК УСТАНОВИТЬ?
##### делает pip install networkx
##### заменяет C:\Program Files\Python36\Lib\site-packages\networkx\algorithms\shortest_paths\dense.py на мой файлик dense.py
## Пример можно, а то не понятно...
```
import networkx as nx
G = nx.gnm_random_graph(15,50)
resu = nx.algorithms.shortest_paths.dense.floyd_warshall(G, do_csv=True)
```
