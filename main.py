import sys

from Printing import printAStar, printBFS, printDFS, printGreedy, printRecursiveBestFirstSearch, printUniformCost
from graphReader import create_graphs

solutions = {
    "bfs": printBFS,
    "dfs": printDFS,
    "greedy": printGreedy,
    "astar": printAStar,
    "uniform": printUniformCost,
    "rbfs": printRecursiveBestFirstSearch
}

def main():
    if len(sys.argv) != 3:
        print("You need to use the following command:\n\npython main.py <filename> <method>")
        print("\nExample:\n\npython main.py ./tests.txt bfs\n")
        print("\nAlternatively, use the following to see result of all method for you tests case:")
        print("python main.py <filename> all")
        return

    tests = sys.argv[1]
    solution_type = sys.argv[2]

    graphs = create_graphs(tests)

    print(f"Running: {tests}")
    if solution_type == "all":
        solutions["bfs"](graphs)
        print()
        solutions["dfs"](graphs)
        print()
        solutions["greedy"](graphs)
        print()
        solutions["astar"](graphs)
        print()
        solutions["uniform"](graphs)
        print()
        solutions["rbfs"](graphs)
    elif solution_type in solutions.keys():
        solutions[solution_type](graphs) 
    else:
        print("Solution method not recognized, running in BFS")
        solutions["bfs"](graphs)
    
if __name__ == "__main__":
    main()
