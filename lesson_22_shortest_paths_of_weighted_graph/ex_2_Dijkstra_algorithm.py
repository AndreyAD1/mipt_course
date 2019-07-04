from collections import deque
from typing import Dict, List


def get_adjacency_list(edges: List[str]) -> Dict[str, Dict[str, int]] or None:
    """
    Return an adjacency list representing a graph.

    Convert the list of strings like 'edge_start, edge_finish, edge_weight' into
    the adjacency list representing a weighted graph.

    :param edges: a list of strings 'edge_start, edge_finish, edge_weight'
    :return: a dictionary {vertex_name: neighbour_vertex_names, ...}
    """
    adjacency_list = {}
    for edge_string in edges:
        try:
            start_vertex, finish_vertex, weight = edge_string.split(', ')
        except ValueError:
            return None

        if start_vertex not in adjacency_list:
            adjacency_list[start_vertex] = {}

        neighbours = adjacency_list[start_vertex]
        neighbours[finish_vertex] = float(weight)

    return adjacency_list


def get_shortest_distances(
        start_vertex_name: str,
        adjacency_list: Dict[str, Dict[str, int]]
) -> Dict[str, int]:
    """
    Return a dict mapping vertex name with distance to this vertex.

    :param start_vertex_name: a name of start vertex
    :param adjacency_list: a structure representing a graph
    :return: a dict {vertex_name_1: distance_to_this_vertex, ...}
    """

    vertex_queue = deque()
    distances = {}
    distances[start_vertex_name] = 0
    vertex_queue.append(start_vertex_name)

    while vertex_queue:
        current_vertex = vertex_queue.popleft()
        for neighbour_vertex, weight in adjacency_list[current_vertex].items():
            new_weight = distances[current_vertex] + weight
            if (
                    neighbour_vertex not in distances or
                    distances[neighbour_vertex] > new_weight
            ):
                distances[neighbour_vertex] = new_weight
                vertex_queue.append(neighbour_vertex)

    return distances


if __name__ == '__main__':
    edge_features = [
        '0, 1, 1',
        '0, 5, 3',
        '0, 2, 0',
        '1, 2, 1',
        '2, 3, 1',
        '3, 4, 1',
        '4, 5, 1',
        '5, 0, 1',
    ]
    adjacency_list = get_adjacency_list(edge_features)
    print(adjacency_list)

    if adjacency_list is None:
        exit('The wrong input data.')

    start_vertex_name = '5'

    if start_vertex_name not in adjacency_list:
        error_message = 'The graph does not contain the start vertex: '
        exit('{} {}.'.format(error_message, start_vertex_name))

    shortest_distances = get_shortest_distances(
        start_vertex_name,
        adjacency_list
    )
    print(shortest_distances)
