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
    pass


def get_interesting_paths_only(
        shortest_paths: List[List],
        starts: List,
        finishes: List
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
    pass


if __name__ == '__main__':
    adjacency_matrix = [[]]
    start_vertexes = [0, 1, 2]
    finish_vertexes = [3, 4, 5]
    shortest_paths = get_shortest_weighted_paths(adjacency_matrix)
    result_matrix = get_interesting_paths_only(
        shortest_paths,
        start_vertexes,
        finish_vertexes
    )
