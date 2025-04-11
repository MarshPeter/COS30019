from Graph import Graph
from collections import deque

class BFS:

    def __init__(self, graph: Graph):
        self.graph = graph

    def breadth_first_search(self):
        explored = set()
        frontier = deque([(self.graph.origin, [self.graph.origin])]) # starts at root node (node, path)
        found_destinations = {}

        while frontier:
            node, path = frontier.popleft()

            # if current node is a destination
            if self.graph.is_goal(node):
                if node not in found_destinations:
                    found_destinations[node] = path
                if len(found_destinations) == len(self.graph.goals):
                    break # found all destinations

            if node not in explored:
                explored.add(node)
                # for neighbour in the list of neighbours...
                for neighbor, _ in self.graph.get_edges(node): # neighbor_node, cost (cost ignored)
                    if neighbor not in explored:
                        frontier.append((neighbor, path + [neighbor]))

        # display all paths       
        return list(found_destinations.items())
