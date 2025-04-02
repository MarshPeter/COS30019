
from math import sqrt
from Graph import Graph

class RecursiveBFS():

    def __init__(self, graph: Graph):
        self.graph = graph

    def rbfs(self):
        results = []
        for goal in self.graph.goals:
            print(goal, self.graph.goals)
            results.append(self.__rbfs([self.graph.origin], 0, float("inf"), goal))

        return results

    def __rbfs(self, path, cost, f_limit, goal):
        curr_node = path[-1]

        f = cost + self.__SLD(curr_node, goal)

        if curr_node == goal:
            return (path, f)

        if f > f_limit:
            return None, f

        successors = []
        # edges in graph are stored as (neighbor, edge_cost)
        for neighbor, edge_cost in self.graph.edges[curr_node]:
            if neighbor in path:
                continue

            new_cost = cost + edge_cost
            f_val = max(new_cost + self.__SLD(neighbor, goal), f)
            successors.append((neighbor, new_cost, f_val))

        if not successors:
            return None, float('inf')

        while True:
            successors.sort(key=lambda x: x[2])
            best = successors[0]
            if best[2] >= f_limit:
                return None, best[2]

            alternative = successors[1][2] if len(successors) > 1 else float('inf')
            new_path, best_f = self.__rbfs(path + [best[0]], best[1], min(f_limit, alternative), goal)
            successors[0] = (best[0], best[1], best_f)
            if new_path is not None:
                return new_path, best_f
        
    def __SLD(self, node, goal):
        try:
            (node_x, node_y) = self.graph.get_position(node)
            (goal_x, goal_y) = self.graph.get_position(goal)
            return sqrt((goal_x - node_x) ** 2 + (goal_y - node_y) ** 2)
        except:
            print(node, goal)
            print(self.graph.node_positions)
            print(self.graph.edges)
            exit(1)
            

