from math import inf

from graphs import Graph, DictGraph


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


def test_dijkstra():
    # Input graph (same as in 'exempleDijkstra.pdf')
    gd = DictGraph({
        'a': {'b': 10, 'd': 5},
        'b': {'c': 1, 'd': 2},
        'c': {'e': 4},
        'd': {'b': 3, 'c': 9, 'e': 2},
        'e': {'a': 7, 'c': 6}
    })

    # Execute dijkstra algorithm
    pred, dist = dijkstra(gd, 'a')

    # Display result
    nodes = sorted(gd.vertices_dict.keys())
    print('sommet ', *(node.ljust(5) for node in nodes))
    print('dist   ', *(str(dist[node]).ljust(5) for node in nodes))
    print('pred   ', *(str(pred[node]).ljust(5) for node in nodes))
    print()


if __name__ == '__main__':
    test_dijkstra()