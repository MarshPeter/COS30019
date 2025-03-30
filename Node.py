
class Node:
    """
    A class representing a point on the graph

    Member Variables:
    number (int): The number of the node on the graph, this is 1-based
    neighbors (List(Tuple(int, int))): The node neighbors of the current node,
        the first element of the tuple is the neighbor number, the second is the cost to reach neighbor
    """
    def __init__(self, number):
        """
        Initialize a Node
        ----------
        number (int): Represents the node number on the graph 
        """
        self.number = number
        self.neighbors = []
