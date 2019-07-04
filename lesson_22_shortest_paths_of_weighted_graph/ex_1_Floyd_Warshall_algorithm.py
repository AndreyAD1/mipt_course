from math import inf
from typing import List


def get_shortest_weighted_paths(adjacency_matrix: List[List]) -> List[List]:
    """
    Return a matrix of shortest distances between weighted graph vertexes.

    This is the implementation of the Floyd–Warshall algorithm.
    Gets adjacency matrix and returns a matrix with shortest distances
    between vertexes.

    :param adjacency_matrix: a list of lists representing a graph
    :return: a list of lists containing the shortest distances between vertexes.
    """
    for vertex_index, vertex in enumerate(adjacency_matrix):
        for neighbour_index, neighbour in enumerate(vertex):
            if neighbour == 0 and vertex_index != neighbour_index:
                adjacency_matrix[vertex_index][neighbour_index] = inf

    vertex_number = len(adjacency_matrix)
    for intermediate_vertex in range(vertex_number):
        for start_vertex in range(vertex_number):
            for finish_vertex in range(vertex_number):
                adjacency_matrix[start_vertex][finish_vertex] = min(
                    adjacency_matrix[start_vertex][finish_vertex],
                    adjacency_matrix[start_vertex][intermediate_vertex] + adjacency_matrix[intermediate_vertex][finish_vertex]
                )
    return adjacency_matrix


def get_interesting_paths_only(
        shortest_paths: List[List],
        starts: List[int],
        finishes: List[int]
) -> List[List]:
    """
    Get only interesting paths from all graph paths

    :param shortest_paths: a list of lists containing the shortest distances
    between vertexes
    :param starts: a list of start vertexes
    :param finishes: a list of finish vertexes
    :return: a list of lists containing distances between interesting start
    and finish vertexes.
    """
    interesting_paths = []

    for start_vertex in starts:
        vertex_paths = []

        for finish_vertex in finishes:
            vertex_paths.append(shortest_paths[start_vertex][finish_vertex])

        interesting_paths.append(vertex_paths)

    return interesting_paths


if __name__ == '__main__':
    adjacency_matrix = [
        [0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0]
    ]
    start_vertexes = [0, 5]
    finish_vertexes = [3, 4, 5]
    shortest_paths = get_shortest_weighted_paths(adjacency_matrix)
    result_matrix = get_interesting_paths_only(
        shortest_paths,
        start_vertexes,
        finish_vertexes
    )
    print(result_matrix)
