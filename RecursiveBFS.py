
from math import sqrt
from Graph import Graph

class RecursiveBestFirstSearch():

    def __init__(self, graph: Graph):
        self.graph = graph

    # loops through all goals and runs the algorithm once for each
    def rbfs(self):
        results = []
        goals_found = 0
        for goal in self.graph.goals:
            explored = set()
            result = self.__rbfs([self.graph.origin], 0, float("inf"), goal, explored)
            if result[0] is not None and len(result[0]) != 0:
                results.append(result[0])
                goals_found += 1
        return results, goals_found

    def __rbfs(self, path, cost, f_limit, goal, explored):
        curr_node = path[-1]

        if curr_node in explored:
            return None, float("inf")

        # A known bug is infinite loops, therefore we have this set that ends cycles after
        # This in turn creates another bug where not all paths are found
        explored.add(curr_node)

        f = cost + self.__SLD(curr_node, goal)

        if curr_node == goal:
            # This is the base case if we find a target
            return (path, f)

        if f >= f_limit:
            # This is the base case if we are giving up on this path
            return None, f

        successors = []
        # edges in graph are stored as (neighbor, edge_cost)
        for neighbor, edge_cost in self.graph.edges[curr_node]:
            if neighbor in path or neighbor in explored:
                continue

            new_cost = cost + edge_cost
            f_val = max(new_cost + self.__SLD(neighbor, goal), f)
            successors.append((neighbor, new_cost, f_val))
        
        # dead end base case
        if not successors:
            return None, float('inf')

        while True:
            # sort successors so that next two best are selected and observed
            successors.sort(key=lambda x: x[2])
            best = successors[0]
            if best[2] >= f_limit:
                return None, best[2]

            alternative = successors[1][2] if len(successors) > 1 else float('inf')

            # recursive call
            new_path, best_f = self.__rbfs(path + [best[0]], best[1], min(f_limit, alternative), goal, explored)
            successors[0] = (best[0], best[1], best_f)

            # This returns the final answer
            if new_path is not None:
                return new_path, best_f
        
    # heuristic function that is the straight line distance
    def __SLD(self, node, goal):
        (node_x, node_y) = self.graph.get_position(node)
        (goal_x, goal_y) = self.graph.get_position(goal)
        return sqrt((goal_x - node_x) ** 2 + (goal_y - node_y) ** 2)
