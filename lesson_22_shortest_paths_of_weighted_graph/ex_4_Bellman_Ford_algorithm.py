from math import inf
from typing import List, Tuple, Dict


def get_shortest_distances(
        vertex_number,
        edge_list: List[Tuple[str, str, int]],
        start_point: str,
) -> Dict[str, int]:
    distances = {start_point: 0}
    for vertex in vertex_number - 1:
        for start_vertex, end_vertex, edge_weight in edge_list:
            if start_vertex not in distances:
                distances[start_vertex] = inf
                distances[end_vertex] = inf
            else:
                distances[end_vertex] = min(
                    distances[end_vertex],
                    distances[start_vertex] + edge_weight
                )
    print('something')
    return distances


if __name__ == '___main__':
    edge_features = [
        ('0', '1', 1),
        ('0', '5', 3),
        ('0', '2', 0),
        ('1', '2', 1),
        ('2', '3', 1),
        ('3', '4', 1),
        ('4', '5', 1),
        ('5', '0', 1),
    ]
    start_point = '0'
    vertex_number = 6
    shortest_distances = get_shortest_distances(
        vertex_number,
        edge_features,
        start_point
    )
    print(shortest_distances)
