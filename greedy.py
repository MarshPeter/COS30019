import heapq
import math
from Graph import Graph

class Greedy:
    """
        Completes a graph problem with a greedy best first search
    """
    def __init__(self, graph: Graph):
        self.graph = graph

    # Heuristic function, heuristic is Straight line distance
    def Hn (self, node, goal):
        x2, y2 = self.graph.node_positions[goal]
        x1, y1 = self.graph.node_positions[node]
        return math.hypot(x2 - x1, y2 - y1)
    
    # Goes through all goals and returns any found results
    def gbfs(self):
        results = []
        for goal in self.graph.goals:
            result = self.__gbfs([self.graph.origin], goal)
            if result is not None:
                results.append(result) # Initialise path list with origin node
        return results
    
    def __gbfs(self, path, goal):
        explored = set()
        frontier = []
        current_node = path[-1]

        # Push origin node with heuristic value to frontier, plus current node and its path
        heapq.heappush(frontier, (self.Hn(current_node, goal), current_node, path)) 

        while frontier:
            # get the next node with minimum cost
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
                # We don't add it if we have already explored it or it is already in the frontier so we don't re-explore it later
                if neighbor not in explored and neighbor not in frontier:
                    # If neighbor node has not been explored, add it to frontier with its path and heuristic value
                    heapq.heappush(frontier, (self.Hn(neighbor, goal), neighbor, path + [neighbor]))
        
        # Destination not found
        return None 



