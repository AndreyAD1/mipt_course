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
        neighbours[finish_vertex] = weight

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

    pass


if __name__ == '__main__':
    vertex_number = 5
    edge_number = 6
    edge_features = [
        '0, 1, 1',
        '0, 5, 10',
        '1, 2, 2',
        '2, 3, 3',
        '3, 4, 4',
        '4, 5, 5',
        '5, 0, 6',

    ]
    adjacency_list = get_adjacency_list(edge_features)
    print(adjacency_list)

    if adjacency_list is None:
        exit('The wrong input data.')

    start_vertex_name = '0'

    if start_vertex_name not in adjacency_list:
        error_message = 'The graph does not contain the start vertex: '
        exit('{} {}.'.format(error_message, start_vertex_name))

    shortest_distances = get_shortest_distances(
        start_vertex_name,
        adjacency_list
    )
    print(shortest_distances)
