from Graph import Graph
from enum import Enum

class FileReadStage(Enum):
    START = 0
    NODES = 1
    EDGES = 2
    ORIGIN = 3
    DESTINATIONS = 4
    END = 5

print("Hello, World!")

def create_graph():
    graph = Graph()
    stage = FileReadStage.START
    with open('./basic_test.txt', 'r') as file:
        for line in file:
            #print(line.strip())
            data = line.strip()
            print(stage)
            stage, changed = update_stage(stage, data)

            if changed: continue

            if stage is FileReadStage.NODES:
                parts = line.split(":")
                neighbor_edge = parts[1].strip()
                node_number = int(parts[0])
                node_x = int(neighbor_edge[1])
                node_y = int(neighbor_edge[-2])
                graph.add_node(node_number, node_x, node_y)
            elif stage is FileReadStage.EDGES:
                parts = line.split(":")
                node_one = int(parts[0][1])
                node_two = int(parts[0][3])
                cost = int(parts[1][1])
                graph.add_neighbor(node_one, node_two, cost)

            # print(graph.node_positions.items())
            print(graph.edges)

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


create_graph()
