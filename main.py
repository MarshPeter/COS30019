import re
from UniformCost import UniformCost
from RecursiveBFS import RecursiveBestFirstSearch
from bfs import BFS
from DFS import DepthFirst
from graphReader import create_graphs
from greedy import Greedy
from AStar import AStar

graphs = create_graphs()
print("Recursive Best First Search:")
graph_count = 0

for graph in graphs:
    problem = RecursiveBestFirstSearch(graph)
    solutions, count = problem.rbfs()
    print(f"In graph {graph_count + 1}: {count} solutions were found out of {len(graph.goals)} goals")
    graph_count += 1
    for solution in solutions:
        print("Start node => ", end="")
        for node in solution:
            print(f"{node} => ", end="")
        print("goal found")

# print("Uniform Cost Search")
# solutions = []

# for graph in graphs:
#     solution = UniformCost(graph)
#     solutions.append(solution.uniform_cost_search())
print("Recursive Best First Search:")
graph_count = 0

for graph in graphs:
    problem = RecursiveBestFirstSearch(graph)
    solutions, count = problem.rbfs()
    print(f"In graph {graph_count + 1}: {count} solutions were found out of {len(graph.goals)} goals")
    graph_count += 1
    for solution in solutions:
        print("Start node => ", end="")
        for node in solution:
            print(f"{node} => ", end="")
        print("goal found")

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
