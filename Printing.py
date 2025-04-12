from AStar import AStar
from DFS import DepthFirst
from RecursiveBFS import RecursiveBestFirstSearch
from UniformCost import UniformCost
from bfs import BFS
from greedy import Greedy

def printRecursiveBestFirstSearch(graphs):
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

def printUniformCost(graphs):
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

def printBFS(graphs):
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

def printDFS(graphs):
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

def printGreedy(graphs):
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

def printAStar(graphs):
    print("A* Search:")
    graph_count = 0

    for graph in graphs:
        problem = AStar(graph)
        solutions = problem.astar()
        print(f"In graph {graph_count + 1}: {len(solutions)} solutions were found for {len(graph.goals)} goals")
        graph_count += 1
        for solution in solutions:
            print("Start node => ", end="")
            for node in solution[1][0]:
                print(f"{node} => ", end="")
            print("goal found")
