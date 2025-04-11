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

print("Uniform Cost Search:")
graph_count = 0

for graph in graphs:
    problem = UniformCost(graph)
    solutions = problem.uniform_cost_search()
    print(f"In graph {graph_count + 1}: {len(solutions)} solutions were found for {len(graph.goals)} goals")
    graph_count += 1
    for solution in solutions:
        print("Start node => ", end="")
        for node in solution[1][0]:
            print(f"{node} => ", end="")
        print("goal found")

print("Breadth First Search:")
graph_count = 0

for graph in graphs:
    problem = BFS(graph)
    solutions = problem.breadth_first_search()
    print(f"In graph {graph_count + 1}: {len(solutions)} solutions were found for {len(graph.goals)} goals")
    graph_count += 1
    for solution in solutions:
        print("Start node => ", end="")
        for node in solution[1]:
            print(f"{node} => ", end="")
        print("goal found")

print("Depth First Search:")
graph_count = 0

for graph in graphs:
    problem = DepthFirst(graph)
    solutions = problem.dfs()
    print(f"In graph {graph_count + 1}: {len(solutions)} solutions were found for {len(graph.goals)} goals")
    graph_count += 1
    for solution in solutions:
        print("Start node => ", end="")
        for node in solution[1][0]:
            print(f"{node} => ", end="")
        print("goal found")

print("Greedy Search:")
graph_count = 0

for graph in graphs:
    problem = Greedy(graph)
    solutions = problem.gbfs()
    print(f"In graph {graph_count + 1}: {len(solutions)} solutions were found for {len(graph.goals)} goals")
    graph_count += 1
    for solution in solutions:
        print("Start node => ", end="")
        for node in solution:
            print(f"{node} => ", end="")
        print("goal found")

# print("Astar")
# solutions = []

# for graph in graphs:
#     solution = AStar(graph)
#     solutions.append(solution.astar())

# print(solutions)
