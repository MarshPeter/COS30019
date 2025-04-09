import heapq
import math
from Graph import Graph

class AStar:
    def __init__(self, graph: Graph):
        self.graph = graph

    def heuristic(self, node, goal):
        x1, y1 = self.graph.node_positions[node]
        x2, y2 = self.graph.node_positions[goal]
        return math.hypot(x2 - x1, y2 - y1)

    def astar(self):
        frontier = []
        heapq.heappush(frontier, (0, 0, self.graph.origin, [self.graph.origin]))
        explored = {}
        found_destinations = {}

        while frontier:
            f, g, node, path = heapq.heappop(frontier)

            if node in explored and explored[node] <= g:
                continue
            explored[node] = g