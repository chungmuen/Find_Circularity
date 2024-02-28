"""
Module to store utility functions for test purposes.
"""
from collections import deque


def build_graph(edges):
    """ Converts a list of directed edges into a graph represented as a dictionary. This function takes a list of
    tuples, where each tuple represents a directed edge from one node to another in the graph. The graph is represented
    as a dictionary where each key is a node and its value is a list of all nodes it has edges to.

    :param: edges (list of tuples): Each tuple contains two elements, representing a directional link from the first
        element (source node) to the second element (destination node).

    :return: dict: A dictionary representation of the graph where keys are source nodes and values are lists of
        destination nodes.

    :example: Given edges [(0, 1), (0, 2), (1, 2), (2, 3)], the function returns
        {0: [1, 2], 1: [2], 2: [3]}.
    """
    graph: dict[int, list] = {}
    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
    return graph


def find_cycles(graph):
    """
    Finds all unique cycles in the graph using a Breadth-First Search (BFS) approach
    and returns them as a list of tuples, where each tuple represents a cycle.

    This function iterates over each node in the graph, using BFS to explore reachable
    nodes. It keeps track of the path taken to reach each node. If it encounters a node
    that completes a cycle back to the starting node, and the set of nodes in the cycle
    has not been encountered before, it records this cycle.

    :param: graph (dict): A graph represented as a dictionary where each key is a node and
        its value is a list of nodes it has edges to.

    :return: list of tuples: Each tuple contains nodes forming a cycle, including the starting
        node repeated at the end to signify the cycle closure.

    :example: Given a graph {0: [1, 2], 1: [2], 2: [3], 3: [0]}, the function may return
        [(0, 1, 2, 3, 0), (0, 2, 3, 0)] as it identifies the cycles in the graph.

    :note: The function ensures that each cycle is unique based on the members of the cycle,
        not the starting point of the cycle in the path. Cycles that contain the same set
        of nodes but start at different points are considered the same and only one is returned.
    """
    cycles = []
    cycles_members = []
    for start_node in graph:
        queue = deque([(start_node, [start_node])])
        while queue:
            current_node, node_path = queue.popleft()
            for neighbor in graph.get(current_node, []):
                cycle_members = set(node_path + [neighbor])
                if neighbor == start_node and cycle_members not in cycles_members:
                    cycles.append(tuple(node_path + [neighbor]))
                    cycles_members.append(cycle_members)
                elif neighbor not in node_path:
                    queue.append((neighbor, node_path + [neighbor]))
    return cycles


# if __name__ == "__main__":
#     edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 0)]
#     graph = build_graph(edges)
#     cycles = find_cycles(graph)
# AVOID HAVING MAIN in a library!
