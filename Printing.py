from AStar import AStar
from DFS import DepthFirst
from RecursiveBFS import RecursiveBestFirstSearch
from UniformCost import UniformCost
from bfs import BFS
from greedy import Greedy

# Note all these printings can work with test cases that contain multiple graphs
# This was the original plan, but it didn't look good, so it was split up, but the
# functionality harms nothing so the ability to do so stays

# All these functions print in every line in the format specified in the assignment for every destination in the graph. That is:
# goal number_of_nodes
# path

def printRecursiveBestFirstSearch(graphs):
    for graph in graphs:
        problem = RecursiveBestFirstSearch(graph)
        solutions, count = problem.rbfs()
        for solution in solutions:
            print(f"{solution[-1]} {count}")
            for node in solution:
                print(f"{node} ", end="")
            print()

def printUniformCost(graphs):
    for graph in graphs:
        problem = UniformCost(graph)
        solutions = problem.uniform_cost_search()
        for solution in solutions:
            print(f"{solution[1][0][-1]} {len(solution[1][0])}")
            for node in solution[1][0]:
                print(f"{node} ", end="")
            print()

def printBFS(graphs):
    for graph in graphs:
        problem = BFS(graph)
        solutions = problem.breadth_first_search()
        for solution in solutions:
            print(f"{solution[1][-1]} {len(solution[1])}")
            for node in solution[1]:
                print(f"{node} ", end="")
            print()

def printDFS(graphs):
    for graph in graphs:
        problem = DepthFirst(graph)
        solutions = problem.dfs()
        for solution in solutions:
            print(f"{solution[1][0][-1]} {len(solution[1][0])}")
            for node in solution[1][0]:
                print(f"{node} ", end="")
            print()

def printGreedy(graphs):
    for graph in graphs:
        problem = Greedy(graph)
        solutions = problem.gbfs()
        for solution in solutions:
            print(f"{solution[-1]} {len(solution)}")
            for node in solution:
                print(f"{node} ", end="")
            print()

def printAStar(graphs):
    for graph in graphs:
        problem = AStar(graph)
        solutions = problem.astar()
        for solution in solutions:
            print(f"{solution[1][0][-1]} {len(solution[1][0])}")
            for node in solution[1][0]:
                print(f"{node} ", end="")
            print()
