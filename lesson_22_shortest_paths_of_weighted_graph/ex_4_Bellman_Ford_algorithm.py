from math import inf
from typing import List, Tuple, Dict


def get_shortest_distances(
        vertex_number,
        edge_list: List[Tuple[str, str, int]],
        start_point: str,
) -> Dict[str, int]:
    distances = {start_point: 0}
    for vertex in range(vertex_number - 1):
        for start_vertex, end_vertex, edge_weight in edge_list:
            if start_vertex in distances:
                distances[end_vertex] = min(
                    distances.get(end_vertex, inf),
                    distances[start_vertex] + edge_weight
                )

    return distances


def get_negative_cycle(
        edge_list: List[Tuple[str, str, int]],
        shortest_distances: Dict[str, int]
) -> Tuple[str, str, int] or None:
    for start_vertex, end_vertex, weight in edge_list:
        if shortest_distances[start_vertex] + weight < shortest_distances[end_vertex]:
            return start_vertex, end_vertex, weight


if __name__ == '__main__':
    edge_features = [
        ('0', '1', 1),
        ('0', '5', -1),
        ('0', '2', 0),
        ('1', '2', 1),
        ('2', '3', 1),
        ('3', '4', 1),
        ('4', '5', 1),
        ('5', '0', -1),
    ]
    start_vertex = '0'
    vertex_number = 6
    shortest_distances = get_shortest_distances(
        vertex_number,
        edge_features,
        start_vertex
    )
    print(shortest_distances)
    negative_cycle = get_negative_cycle(edge_features, shortest_distances)
    print('Negative cycle: {}'.format(negative_cycle))
