import heapq
import math
from Graph import Graph

class Greedy:
    def __init__(self, graph: Graph):
        self.graph = graph

    # Heuristic function
    def Hn (self, node, goal):
        x1, y1 = self.graph.node_positions[node]
        x2, y2 = self.graph.node_positions[goal]
        return math.hypot(x2 - x1, y2 - y1)
    
    def gbfs(self):
        results = []
        for goal in self.graph.goals:
            print(goal, self.graph.goals)
            results.append(self.__gbfs([self.graph.origin], goal)) # Initialise path list with origin node
        return results
    
    def __gbfs(self, path, goal):
        explored = set()
        frontier = []
        current_node = path[-1]

        # Push origin node with heuristic value to frontier, plus current node and its path
        heapq.heappush(frontier, (self.Hn(current_node, goal), current_node, path)) 

        while frontier:
            _, current_node, path = heapq.heappop(frontier)

            # Skip node if it has already been explored
            if current_node in explored:
                continue
            
            explored.add(current_node)

            # If the goal node has been reached, return the path
            if current_node == goal:
                return path # Path from origin to goal
            
            # Exploring neighbors
            for neighbor, _ in self.graph.get_edges(current_node):
                if neighbor not in explored:
                    # If neighbor node has not been explored, add it to frontier with its path and heuristic value
                    heapq.heappush(frontier, (self.Hn(neighbor, goal), neighbor, path + [neighbor]))
        
        # Destination not found
        return None 



