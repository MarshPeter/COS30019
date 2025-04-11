import re
from UniformCost import UniformCost
from RecursiveBFS import RecursiveBFS
from bfs import BFS
from DFS import DepthFirst
from graphReader import create_graphs
from greedy import Greedy
from AStar import AStar

graphs = create_graphs()
print("Recursive Best First Search:")
solutions = []

for graph in graphs:
    solution = RecursiveBFS(graph)
    solutions.append(solution.rbfs())

print(solutions)
# print("Uniform Cost Search")
# solutions = []

# for graph in graphs:
#     solution = UniformCost(graph)
#     solutions.append(solution.uniform_cost_search())

# print(solutions)

# print("BFS")
# solutions = []

# for graph in graphs:
#     solution = BFS(graph)
#     solutions.append(solution.breadth_first_search())

# print(solutions)

# print("DFS")
# solutions = []

# for graph in graphs:
#     solution = DepthFirst(graph)
#     solutions.append(solution.dfs())

# print(solutions)

# print("Greedy")
# solutions = []

# for graph in graphs:
#     solution = Greedy(graph)
#     solutions.append(solution.gbfs())

# print(solutions)

# print("Astar")
# solutions = []

# for graph in graphs:
#     solution = AStar(graph)
#     solutions.append(solution.astar())

# print(solutions)
