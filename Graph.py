from collections import defaultdict

class Graph:
    """
    Contains the state of a map, node that all nodes on the graph are 1-based all values start uninitialized
    Member Variables:
    origin (int || None): The origin node
    goals (List[int] || None): A list of all possible goals
    nodes (dict(int, List[Tuple(int, int)]) || None): A dictionary that contains all nodes on a map represented
        by their numbers (whihc are 1-based) that maps to their neighbors as a List of Tuples. The first
        element is the neighbor node number, the second variable is the cost to reach that node
    """
    def __init__(self):
        self.origin = None
        self.goals = None
        self.edges = defaultdict(list)
        self.node_positions = defaultdict(tuple) # {node_number: x, y}

    def add_node(self, node, pos_x, pos_y):
        self.node_positions[node] = (pos_x, pos_y)

    def set_origin(self, origin):
        self.origin = origin

    def set_goals(self, goals):
        self.goals = goals

    def add_neighbor(self, node, neighbor_node, cost):
        self.edges[node].append((neighbor_node, cost))

    def is_goal(self, node):
        return node in self.goals

    def get_edges(self, node):
        return self.edges[node]
