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
