from unittest import TestCase

from libs.utils import find_cycles


class TestFindCycles(TestCase):
    # the name of the class is the name of the file
    """
    ex: there are methods that are executed before/after all or each tests, cleans variables, ex, resetting global
    variables between sets of tests
    """

    def setUp(self) -> None:
        """set up method is executed before each test, and that allows sharing data between tests"""
        self.input_graph = {0: [1, 2], 1: [2], 2: [3], 3: [0]}

    def test_find_cycles(self):
        """
        Tests the find_cycles function for its ability to accurately identify all unique cycles in a graph.

        This test assesses whether the find_cycles function can take a graph represented as a dictionary
        and return a list of tuples, each representing a unique cycle found within the graph. A cycle is
        defined as a path that starts and ends at the same node without traversing any node more than once,
        except for the starting/ending node.

        The assertIn method is used to verify that each expected cycle is present in the function's output,
        demonstrating the function's effectiveness in cycle detection.
        """
        # the name of the function is the function we are testing
        expected_output = [(0, 2, 3, 0), (0, 1, 2, 3, 0)]
        for cycle in expected_output:
            self.assertIn(cycle, find_cycles(self.input_graph))
