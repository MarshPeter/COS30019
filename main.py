from UniformCost import UniformCost
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

print("Hello, World!")

# returns a list of Graph objects based of file read
def create_graphs():
    graphs = []
    graph = Graph()
    stage = FileReadStage.START

    # read file, auto close when at EOF
    with open('./multi_tests.txt', 'r') as file:
        for line in file:
            data = line.strip() # remove whitespace

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
                parts = line.split(":")
                neighbor_edge = parts[1].strip()
                node_number = int(parts[0])
                node_x = int(neighbor_edge[1])
                node_y = int(neighbor_edge[-2])
                graph.add_node(node_number, node_x, node_y)
            elif stage is FileReadStage.EDGES:
                # read in edges and add them to current graph
                # all edges in form: (2,1): 2
                parts = line.split(":")
                node_one = int(parts[0][1])
                node_two = int(parts[0][3])
                cost = int(parts[1][1])
                graph.add_neighbor(node_one, node_two, cost)
            elif stage is FileReadStage.ORIGIN:
                # read in origin and add to current graph
                # all origins in form: 1
                graph.set_origin(int(line[0]))
            elif stage is FileReadStage.DESTINATIONS:
                # read in destinations and add to current graph
                # all destinations are in form: 5; 4
                parts = [int(x.strip()) for x in line.split(";")]
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
    solution = UniformCost(graph)
    solutions.append(solution.uniform_cost_search())

print(solutions)
