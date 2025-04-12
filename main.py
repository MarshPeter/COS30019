import sys
from Printing import printAStar, printBFS, printDFS, printGreedy, printRecursiveBestFirstSearch, printUniformCost
from graphReader import create_graphs

# methods available to use for solution
solutions = {
    "bfs": printBFS,
    "dfs": printDFS,
    "greedy": printGreedy,
    "astar": printAStar,
    "uniform": printUniformCost,
    "rbfs": printRecursiveBestFirstSearch # per report, this one isn't entirely accurate, but won't break or infinite cycle
}

def main():
    # Confirms format + provides help info
    if len(sys.argv) != 3:
        print("You need to use the following command:\n\npython main.py <filename> <method>")
        print("\nExample:\n\npython main.py ./tests.txt bfs\n")
        print("\nOptions:")
        print("bfs: Breadth First Search")
        print("dfs: Depth First Search")
        print("greedy: Greedy Best First Search")
        print("astar: A* Search")
        print("uniform: Uniform-Cost Search")
        print("rbfs: Recursive Best First Search\n")
        print("\nAlternatively, use the following to see result of all method for you tests case:")
        print("python main.py <filename> all\n")
        return

    # assumes user inputs correct information
    tests = sys.argv[1]
    solution_type = sys.argv[2]

    # retrieve all graphs of test case (provided ones are one off test cases, but can handle multiple graphs in a single test case)
    graphs = create_graphs(tests)

    # info print for the first line of specified output in the report of form: filename method
    print(f"{tests} {solution_type}")
    
    # for easier comparison
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
        solutions["rbfs"](graphs) # This method doesn't print all nodes because of a known issue that is a bug fix for a infinite loop caused by cycles.
    elif solution_type in solutions.keys():
        # specific solution
        solutions[solution_type](graphs) 
    else:
        # defaults to bfs output
        print("Solution method not recognized, running in BFS")
        solutions["bfs"](graphs)
    
if __name__ == "__main__":
    main()
