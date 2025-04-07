import re
from UniformCost import UniformCost
from RecursiveBFS import RecursiveBFS
from bfs import  BFS
from Graph import Graph
from enum import Enum

# Current stage of a graph being read
class FileReadStage(Enum):
    START = 0 # we are starting a new graph
    NODES = 1 # we are reading nodes
    EDGES = 2 # we are reading edges
    ORIGIN = 3 # we are reading the origin
    DESTINATIONS = 4 # we are reading the destinations
    END = 5 # We have completed the graph

# returns a list of Graph objects based of file read
def create_graphs():
    graphs = []
    graph = Graph()
    stage = FileReadStage.START

    # read file, auto close when at EOF
    with open('./test_three.txt', 'r') as file:
        for line in file:
            data = line.strip() # remove whitespace

            # skip blank lines (usually end of file in generated tests)
            if data == "":
                continue

            # If this file holds multiple graphs, this starts a new graph after one is finished
            if stage == FileReadStage.END and data == "Nodes:":
                graph = Graph()
                stage = FileReadStage.START

            stage, changed = update_stage(stage, data)
            
            # Stage of graph read has changed, but we need new line for data
            if changed: continue

            if stage is FileReadStage.NODES:
                # Read in nodes and add them to current graph
                # All nodes in form: 1: (4, 1)
                values = re.findall(r'\d+', line)
                node_number = int(values[0])
                node_x = int(values[1])
                node_y = int(values[2])
                graph.add_node(node_number, node_x, node_y)
            elif stage is FileReadStage.EDGES:
                # read in edges and add them to current graph
                # all edges in form: (2,1): 2
                values = re.findall(r'\d+', line)
                node_one = int(values[0])
                node_two = int(values[1])
                cost = int(values[2])
                graph.add_neighbor(node_one, node_two, cost)
            elif stage is FileReadStage.ORIGIN:
                # read in origin and add to current graph
                # all origins in form: 1
                values = re.findall(r'\d+', line)
                graph.set_origin(int(values[0]))
            elif stage is FileReadStage.DESTINATIONS:
                # read in destinations and add to current graph
                # all destinations are in form: 5; 4
                parts = [int(x.strip()) for x in line.split(";") if x.strip() != ""]
                graph.set_goals(parts)
                stage = FileReadStage.END
                graphs.append(graph)

    return graphs

def update_stage(current_stage, line):
    if line == "Nodes:":
        return FileReadStage.NODES, True
    elif line == "Edges:":
        return FileReadStage.EDGES, True
    elif line == "Origin:":
        return FileReadStage.ORIGIN, True
    elif line == "Destinations:":
        return FileReadStage.DESTINATIONS, True
    return current_stage, False

graphs = create_graphs()
solutions = []

for graph in graphs:
    solution = RecursiveBFS(graph)
    solutions.append(solution.rbfs())

print(solutions)
solutions = []

for graph in graphs:
    solution = UniformCost(graph)
    solutions.append(solution.uniform_cost_search())

print(solutions)
solutions = []

for graph in graphs:
    solution = BFS(graph)
    solutions.append(solution.breadth_first_search())

print(solutions)