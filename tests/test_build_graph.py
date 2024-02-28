from unittest import TestCase

from libs.utils import build_graph

INPUT_EDGES = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 0)]


class TestBuildGraph(TestCase):
    # the name of the class is the name of the file
    """
    ex: there are methods that are executed before/after all or each tests, cleans variables, ex, resetting global
    variables between sets of tests
    """

    def test_build_graph(self):
        """
        Tests the build_graph function to ensure it correctly converts a list of edges into a graph.

        This test verifies that the build_graph function takes a list of tuples, where each tuple
        represents a directed edge in the graph, and returns a dictionary representation of the graph.
        The keys of the dictionary are source nodes, and the values are lists of destination nodes
        that the source node has edges to.
        """
        # the name of the function is the function we are testing
        expected_output = {0: [1, 2], 1: [2], 2: [3], 3: [0]}
        self.assertEqual(build_graph(INPUT_EDGES), expected_output)
