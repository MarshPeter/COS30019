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
    print('argument list', sys.argv)

    if len(sys.argv) != 3:
        print("You need to use the following command:\n\npython main.py <filename> <method>")
        print("\nExample:\n\npython main.py ./tests.txt bfs\n")
        return

    tests = sys.argv[1]
    solution_type = sys.argv[2]

    graphs = create_graphs(tests)
    solutions[solution_type](graphs) 
    
if __name__ == "__main__":
    main()
