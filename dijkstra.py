#!/usr/bin/env python3

from math import inf


class Graph:
    def __init__(self, weights_matrix):
        self.weights_matrix = weights_matrix
        self.nb_vertices = len(self.weights_matrix)
        self.vertices = list(range(self.nb_vertices))

    def weight(self, from_vertex, to_vertex):
        return self.weights_matrix[from_vertex][to_vertex]

    def get_adj(self, vertex):
        for v, w in enumerate(self.weights_matrix[vertex]):
            if w != 0 and w != inf:
                yield v


def dijkstra(graph: Graph, first_vertex):
    dist = {vertex: inf for vertex in graph.vertices}
    dist[first_vertex] = 0
    pred = {vertex: None for vertex in graph.vertices}

    pq = sorted(dist.keys(), key=dist.get)
    path = []

    while len(pq) > 0:
        u = pq.pop(pq.index(min(pq)))
        path.append(u)
        for v in graph.get_adj(u):
            u_plus_weight = graph.weight(u, v)
            if dist[v] > dist[u] + u_plus_weight:
                dist[v] = dist[u] + u_plus_weight
                pred[v] = u

    return pred, dist


#                 0    1    2    3    4
graph = Graph([[  0,   2,   4, inf,   3],  # 0
               [  2,   0,   8, inf,   1],  # 1
               [  6,   2,   0,   4,   3],  # 2
               [  1, inf, inf,   0,   5],  # 3
               [inf, inf, inf,   1,   0]]) # 4

print(dijkstra(graph, 0))
