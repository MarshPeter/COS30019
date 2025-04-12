import heapq
import math
from Graph import Graph

class AStar:
    """
        Completes a graph problem with a A* search
    """
    def __init__(self, graph: Graph):
        self.graph = graph

    # Heuristic function, heuristic is straight line distance
    def heuristic(self, node, goal):
        x1, y1 = self.graph.node_positions[node]
        x2, y2 = self.graph.node_positions[goal]
        return math.hypot(x2 - x1, y2 - y1)

    # solves the problem, and returns all found solutions in one call
    def astar(self):
        frontier = []
        # utilizes a min-heap, we store it with f, g, node, path to node
        heapq.heappush(frontier, (0, 0, self.graph.origin, [self.graph.origin]))
        # keeps track of nodes we have explored
        explored = {}
        # keeps track of destinations we have already found
        found_destinations = {}

        # while frontier is not empty
        while frontier:
            # We don't use f when we pop the next node, but we use the rest
            _, g, node, path = heapq.heappop(frontier)

            # if we have already investigated the node and that evaluation was less, we ignore this node and try another, it cannot be a optimal solution
            if node in explored and explored[node] <= g:
                continue

            # We store a pair of node and total host
            explored[node] = g

            # add path into found_destinations and then return the list if we found everything
            if self.graph.is_goal(node):
                if node not in found_destinations:
                    found_destinations[node] = (path, len(explored))
                if len(found_destinations) == len(self.graph.goals):
                    return list(found_destinations.items())

            # calculate f for all neighbors and add them to the frontier
            for neighbor, cost in self.graph.get_edges(node):
                new_g = g + cost
                h = min([self.heuristic(neighbor, goal) for goal in self.graph.goals])
                new_f = new_g + h
                heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

        return list(found_destinations.items())
