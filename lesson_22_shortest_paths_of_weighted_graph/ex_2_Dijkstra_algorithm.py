from typing import Dict, List


def get_adjacency_list(edges: List[str]) -> Dict[str, set]:
    """
    Return an adjacency list representing a graph.

    Convert the list of strings like 'edge_start, edge_finish, edge_weight' into
    the adjacency list representing the graph.

    :param edges: a list of strings 'edge_start, edge_finish, edge_weight'
    :return: a dictionary {vertex_name: neighbour_vertexe_names, ...}
    """
    pass


def get_shortest_distances(
        start_vertex_name: str,
        adjacency_list: Dict[str, set]
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
        '1, 2, 2',
        '2, 3, 3',
        '3, 4, 5',
        '4, 5, 6',
        '5, 0, 7',
    ]
    adjacency_list = get_adjacency_list(edge_features)
    start_vertex_name = '0'

    if start_vertex_name not in adjacency_list:
        error_message = 'The graph does not contain the start vertex: '
        exit('{} {}.'.format(error_message, start_vertex_name))

    shortest_distances = get_shortest_distances(
        start_vertex_name,
        adjacency_list
    )
    print(shortest_distances)
