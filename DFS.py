from Graph import Graph

class DepthFirst:
    def __init__(self, graph: Graph):
        self.graph = graph

    def dfs(self):
        stack = [(self.graph.origin, [self.graph.origin])]
        visited = set()
        found_destinations = {}

        while stack:
            node, path = stack.pop()

            if node in visited:
                continue
            visited.add(node)

            if self.graph.is_goal(node):
                if node not in found_destinations:
                    found_destinations[node] = (path, len(visited))
                if len(found_destinations) == len(self.graph.goals):
                    return list(found_destinations.items())

            for neighbor, _ in sorted(self.graph.get_edges(node), reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

        return list(found_destinations.items())
