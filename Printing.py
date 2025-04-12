from AStar import AStar
from DFS import DepthFirst
from RecursiveBFS import RecursiveBestFirstSearch
from UniformCost import UniformCost
from bfs import BFS
from greedy import Greedy

# Note all these printings can work with test cases that contain multiple graphs
# This was the original plan, but it didn't look good, so it was split up, but the
# functionality harms nothing so the ability to do so stays

def printRecursiveBestFirstSearch(graphs):
    print("Recursive Best First Search".center(100, "-"))

    for graph in graphs:
        problem = RecursiveBestFirstSearch(graph)
        solutions, count = problem.rbfs()
        print(f"With an origin of {graph.origin}: {count} solutions were found out of {len(graph.goals)} goals for a graph with {len(graph.node_positions)} nodes")
        for solution in solutions:
            print(f"\ngoal = {solution[-1]}")
            for node in solution:
                print(f"{node} => ", end="")
            print("goal found")
    print("".center(100, "-"))

def printUniformCost(graphs):
    print("Uniform Cost Search".center(100, "-"))

    for graph in graphs:
        problem = UniformCost(graph)
        solutions = problem.uniform_cost_search()
        print(f"With an origin of {graph.origin}: {len(solutions)} solutions were found for {len(graph.goals)} goals for a graph with {len(graph.node_positions)} nodes")
        for solution in solutions:
            print(f"\ngoal = {solution[1][0][-1]}")
            for node in solution[1][0]:
                print(f"{node} => ", end="")
            print("goal found")
    print("".center(100, "-"))

def printBFS(graphs):
    print("Breadth First Search".center(100, "-"))

    for graph in graphs:
        problem = BFS(graph)
        solutions = problem.breadth_first_search()
        print(f"With an origin of {graph.origin}: {len(solutions)} solutions were found for {len(graph.goals)} goals for a graph with {len(graph.node_positions)} nodes")
        for solution in solutions:
            print(f"\ngoal = {solution[1][-1]}")
            for node in solution[1]:
                print(f"{node} => ", end="")
            print("goal found")
    print("".center(100, "-"))

def printDFS(graphs):
    print("Depth First Search".center(100, "-"))

    for graph in graphs:
        problem = DepthFirst(graph)
        solutions = problem.dfs()
        print(f"With an origin of {graph.origin}: {len(solutions)} solutions were found for {len(graph.goals)} goals for a graph with {len(graph.node_positions)} nodes")
        for solution in solutions:
            print(f"\ngoal = {solution[1][0][-1]}")
            for node in solution[1][0]:
                print(f"{node} => ", end="")
            print("goal found")
    print("".center(100, "-"))

def printGreedy(graphs):
    print("Greedy Search".center(100, "-"))

    for graph in graphs:
        problem = Greedy(graph)
        solutions = problem.gbfs()
        for solution in solutions:
            print(f"{solution[-1]} {len(graph.nodes)}")
            for node in solution:
                print(f"{node} => ", end="")
            print("goal found")
    print("".center(100, "-"))

def printAStar(graphs):
    print("A* Search".center(100, "-"))

    for graph in graphs:
        problem = AStar(graph)
        solutions = problem.astar()
        print(f"With an origin of {graph.origin}: {len(solutions)} solutions were found for {len(graph.goals)} goals for a graph with {len(graph.node_positions)} nodes")
        for solution in solutions:
            print(f"\ngoal = {solution[1][0][-1]}")
            for node in solution[1][0]:
                print(f"{node} => ", end="")
            print("goal found")
    print("".center(100, "-"))
