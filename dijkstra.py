#!/usr/bin/env python3

from math import inf
from typing import Iterable


class Graph:
    def __init__(self, nb_vertices, vertices):
        self.nb_vertices = nb_vertices
        self.vertices = vertices

    def weight(self, from_vertex, to_vertex) -> int:
        pass

    def get_adj(self, vertex) -> Iterable:
        pass


class MatrixGraph(Graph):
    def __init__(self, weights_matrix):
        self.weights_matrix = weights_matrix
        nb_vertices = len(self.weights_matrix)
        vertices = list(range(nb_vertices))
        super().__init__(nb_vertices, vertices)

    def weight(self, from_vertex, to_vertex):
        return self.weights_matrix[from_vertex][to_vertex]

    def get_adj(self, vertex):
        for v, w in enumerate(self.weights_matrix[vertex]):
            if w != 0 and w != inf:
                yield v


class DictGraph(Graph):
    def __init__(self, vertices_dict):
        self.vertices_dict = vertices_dict
        nb_vertices = len(self.vertices_dict)
        super().__init__(nb_vertices, vertices_dict.keys())

    def weight(self, from_vertex, to_vertex):
        return self.vertices_dict[from_vertex][to_vertex]

    def get_adj(self, vertex):
        yield from self.vertices_dict[vertex].keys()


def dijkstra(graph: Graph, first_vertex):
    dist = {vertex: inf for vertex in graph.vertices}
    dist[first_vertex] = 0
    pred = {vertex: None for vertex in graph.vertices}

    pq = sorted(dist.keys(), key=dist.get)
    path = []

    while len(pq) > 0:
        u = pq.pop(pq.index(min(pq, key=dist.get)))
        path.append(u)
        for v in graph.get_adj(u):
            weight_plus_uv = dist[u] + graph.weight(u, v)
            if dist[v] > weight_plus_uv:
                dist[v] = weight_plus_uv
                pred[v] = u

    return pred, dist


#                 0    1    2    3    4
gm = MatrixGraph([[  0,   2,   4, inf,   3],  # 0
                  [  2,   0,   8, inf,   1],  # 1
                  [  6,   2,   0,   4,   3],  # 2
                  [  1, inf, inf,   0,   5],  # 3
                  [inf, inf, inf,   1,   0]]) # 4

gd = DictGraph({
    'a': {'b': 10, 'd': 5},
    'b': {'c': 1, 'd': 2},
    'c': {'e': 4},
    'd': {'b': 3, 'c': 9, 'e': 2},
    'e': {'a': 7, 'c': 6}
})


print(dijkstra(gm, 0))
print(dijkstra(gd, 'a'))
