# Алгоритм floyd_warshall на графах
## ЗАЧЕМ?
##### Прост) (На самом дела, это довольно-таки интересный алгоритм, потому что он за n^3 дает придельно много информации о графе.)
## КАК УСТАНОВИТЬ?
##### pip install networkx
##### replace C:\Program Files\Python36\Lib\site-packages\networkx\algorithms\shortest_paths\dense.py -> dense.py
## КАК ИСПОЛЬЗОВАТЬ?
### Пример:
```
import networkx as nx
G = nx.gnm_random_graph(15,50)
nx.algorithms.shortest_paths.dense.floyd_warshall(G, do_csv=True)

# Альтернатива
# ставим dense.py в корень проета
import dense as d
G = nx.gnm_random_graph(15,50)
d.floyd_warshall(G, do_csv=True)
```
##### после floyd_warshall() в корне папки будет файлик
