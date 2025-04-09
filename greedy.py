import heapq
import math
from Graph import Graph

class Greedy:
    def __init__(self, graph: Graph):
        self.graph = graph

    #heuristic function
    def hn (self, node, goal):
        x1, y1 = self.graph.node_positions[node]
        x2, y2 = self.graph.node_positions[node]
        return math.hypot(x2 - x1, y2 - y1)


