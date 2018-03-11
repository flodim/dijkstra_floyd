from math import inf

from graphs import Graph, MatrixGraph


def floyd(graph: Graph):
    dist = graph.weights_matrix
    for k in range(graph.nb_vertices):
        for i in range(graph.nb_vertices):
            for j in range(graph.nb_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def test_floyd():
    # Input graph (same as in '01_algo_av_graphs_slides-1.pdf')
    #                    0    1    2    3    4
    gm = MatrixGraph([[0, 2, 4, inf, 3],  # 0
                      [2, 0, 8, inf, 1],  # 1
                      [6, 2, 0, 4, 3],  # 2
                      [1, inf, inf, 0, 5],  # 3
                      [inf, inf, inf, 1, 0]])  # 4

    # Execute floyd algorithm
    dist = floyd(gm)

    # Display result
    for line in dist:
        print(*line, sep=' ')

if __name__ == '__main__':
    test_floyd()