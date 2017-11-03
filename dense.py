# -*- coding: utf-8 -*-
"""Floyd-Warshall algorithm for shortest paths.
"""
#    Copyright (C) 2004-2017 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

import networkx as nx
__author__ = """Aric Hagberg <aric.hagberg@gmail.com>"""
__all__ = ['floyd_warshall',
           'floyd_warshall_predecessor_and_distance',
           'floyd_warshall_numpy']


def floyd_warshall_numpy(G, nodelist=None, weight='weight'):
    """Find all-pairs shortest path lengths using Floyd's algorithm.

    Parameters
    ----------
    G : NetworkX graph

    nodelist : list, optional
       The rows and columns are ordered by the nodes in nodelist.
       If nodelist is None then the ordering is produced by G.nodes().

    weight: string, optional (default= 'weight')
       Edge data key corresponding to the edge weight.

    Returns
    -------
    distance : NumPy matrix
        A matrix of shortest path distances between nodes.
        If there is no path between to nodes the corresponding matrix entry
        will be Inf.

    Notes
    ------
    Floyd's algorithm is appropriate for finding shortest paths in
    dense graphs or graphs with negative weights when Dijkstra's
    algorithm fails.  This algorithm can still fail if there are
    negative cycles.  It has running time $O(n^3)$ with running space of $O(n^2)$.
    """
    try:
        import numpy as np
    except ImportError:
        raise ImportError(
            "to_numpy_matrix() requires numpy: http://scipy.org/ ")

    # To handle cases when an edge has weight=0, we must make sure that
    # nonedges are not given the value 0 as well.
    A = nx.to_numpy_matrix(G, nodelist=nodelist, multigraph_weight=min,
                           weight=weight, nonedge=np.inf)
    n, m = A.shape
    I = np.identity(n)
    A[I == 1] = 0  # diagonal elements should be zero
    for i in range(n):
        A = np.minimum(A, A[i, :] + A[:, i])
    return A


def floyd_warshall_predecessor_and_distance(G, weight='weight'):
    """Find all-pairs shortest path lengths using Floyd's algorithm.

    Parameters
    ----------
    G : NetworkX graph

    weight: string, optional (default= 'weight')
       Edge data key corresponding to the edge weight.

    Returns
    -------
    predecessor,distance : dictionaries
       Dictionaries, keyed by source and target, of predecessors and distances
       in the shortest path.

    Notes
    ------
    Floyd's algorithm is appropriate for finding shortest paths
    in dense graphs or graphs with negative weights when Dijkstra's algorithm
    fails.  This algorithm can still fail if there are negative cycles.
    It has running time $O(n^3)$ with running space of $O(n^2)$.

    See Also
    --------
    floyd_warshall
    floyd_warshall_numpy
    all_pairs_shortest_path
    all_pairs_shortest_path_length
    """
    from collections import defaultdict
    # dictionary-of-dictionaries representation for dist and pred
    # use some defaultdict magick here
    # for dist the default is the floating point inf value
    dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for u in G:
        dist[u][u] = 0
    pred = defaultdict(dict)
    # initialize path distance dictionary to be the adjacency matrix
    # also set the distance to self to 0 (zero diagonal)
    undirected = not G.is_directed()
    for u, v, d in G.edges(data=True):
        e_weight = d.get(weight, 1.0)
        dist[u][v] = min(e_weight, dist[u][v])
        pred[u][v] = u
        if undirected:
            dist[v][u] = min(e_weight, dist[v][u])
            pred[v][u] = v

    vertexes_len = len(pred.items()) #
    iterationNum = 1
    result = []
    for w in G:
        for u in G:
            for v in G:
                if dist[u][v] > dist[u][w] + dist[w][v]:
                    dist[u][v] = dist[u][w] + dist[w][v]
                    pred[u][v] = pred[w][v]

        # my logic
        pred_tablee = []
        for k, v in pred.items():
            all_cells = [0 for i in range(vertexes_len)]
            
            for kk, vv in v.items():
                all_cells[kk] = vv

            pred_tablee.append(all_cells)
        
        dist_tablee = []
        for k, v in dist.items():
            all_cells = [0 for i in range(vertexes_len)]
            
            for kk, vv in v.items():
                all_cells[kk] = vv

            dist_tablee.append(all_cells)
        
        # print(tablee)
        # import_obj_to_csv(dist_tablee, pred_tablee, iterationNum)
        result.append(
            {
                'iterName' : iterationNum,
                'prevTable' : pred_tablee,
                'distTable' : dist_tablee
            }
        )
        iterationNum+=1
        print('-'*30)
        # END _ my logic
    
    import_obj_to_csv(result)

    return dict(pred), dict(dist)

def import_obj_to_csv(objectFile):
    
    do_print = False
    do_json = False
    do_csv = True

    #              1
    # ======== print pretty way ========
    if do_print:
        import pprint
        pprint.pprint(objectFile)



    #              2
    # ======== make .json ========
    if do_json:
        import json
        with open('result_tables.json', 'w+') as outfile:
            json.dump(objectFile, outfile)
    


    # ======== make .csv ========
    if do_csv:
        import csv
        import datetime

        # let's create some name for our output file
        filename = '{0:%Y-%m-%d %H-%M-%S}'.format(datetime.datetime.now()) + ' result_tables.csv'

        with open(filename, 'w+', newline='') as file:

            # let's choose 
            #       delimiter='\t'
            # and   dialect='excel'
            writer = csv.writer(file, delimiter='\t', dialect='excel')

            # TIP
            # for printing text use:
            # writer.writerow(['yourText']), instead of writer.writerow('yourText')
            # coz that's more pretty :)
            for item in objectFile:
                writer.writerow( 'iteration #' + str(item['iterName']))
                writer.writerow([' '])

                writer.writerow(['PREV TABLE'])
                writer.writerows(item['prevTable'])
                writer.writerow([' '])

                writer.writerow(['DIST TABLE'])
                writer.writerows(item['distTable'])
                writer.writerow([' '])
                
                writer.writerow('=============')
    
    

def floyd_warshall(G, weight='weight'):
    """Find all-pairs shortest path lengths using Floyd's algorithm.

    Parameters
    ----------
    G : NetworkX graph

    weight: string, optional (default= 'weight')
       Edge data key corresponding to the edge weight.


    Returns
    -------
    distance : dict
       A dictionary,  keyed by source and target, of shortest paths distances
       between nodes.

    Notes
    ------
    Floyd's algorithm is appropriate for finding shortest paths
    in dense graphs or graphs with negative weights when Dijkstra's algorithm
    fails.  This algorithm can still fail if there are negative cycles.
    It has running time $O(n^3)$ with running space of $O(n^2)$.

    See Also
    --------
    floyd_warshall_predecessor_and_distance
    floyd_warshall_numpy
    all_pairs_shortest_path
    all_pairs_shortest_path_length
    """
    # could make this its own function to reduce memory costs
    return floyd_warshall_predecessor_and_distance(G, weight=weight)[1]

# fixture for nose tests


def setup_module(module):
    from nose import SkipTest
    try:
        import numpy
    except:
        raise SkipTest("NumPy not available")
