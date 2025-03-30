import heapq
import Graph

class UniformCost:

    def __init__(self, graph: Graph):
        self.graph = graph

    def uniform_cost_search(self):
        frontier = []
        frontier = heapq.heappush(frontier, [0, self.graph.origin, [self.graph.origin]]) 
        explored = {}
        found_destinations = {}

        while frontier:
            cost, node, path = heapq.heappop(frontier)

            if self.graph.is_goal(node):
                if node not in found_destinations:
                    found_destinations[node] = (path, cost)
                if len(found_destinations) == len(self.graph.goals):
                    return found_destinations.items()

            if node in explored and cost <= explored[node]:
                continue

            explored[node] = cost

            # returns List(Tuple(node_neighbour_number, edge_cost))
            edges = self.graph.get_edges(node)

            for edge in edges:
                cumulative = cost + edge[1]
                new_path = path + [edge[0]]
                heapq.heappush(frontier, (cumulative, edge[0], new_path))

        # If there is no valid path
        return None, float('inf')
