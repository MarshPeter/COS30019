from math import floor
from collections import defaultdict
import random

def write_tests():
    """
        writes tests in specified format of the report. Can re-run to re-generate test_1 ... test_12 in the tests directory. Creates a random number between 10 and 50 nodes, and constructs a graph based off of that. All edges added are one way, therefore for two way travel, two edges need to be added in both directions. This means that edges = n are not guaranteed to be 100% solvable
    """
    test_count = 0
    max_tests = 12 # change this number to add more tests ot tests folder
    while test_count < max_tests:
        current_file_name = f"./tests/test_{test_count + 1}.txt" # have variable name or each test will overwrite eachother
        test_count += 1
        with open(current_file_name, "w") as file:
            nodes = max(floor(random.random() * 50) + 1, 10) # randomize node count, change to have more / less nodes. Always have at least 5 to prevent issues
            taken_positions = defaultdict(list) # maps nodes to positions to stop nodes from spawning at same position {node: [x, y]} 

            file.write("Nodes:\n")

            # Generate and add nodes to graph until we have nodes amount of nodes
            for i in range(nodes):
                x = 0
                y = 0

                while True:
                    x = floor(random.random() * nodes * 2)
                    y = floor(random.random() * nodes * 2)
                    # check for already taken position
                    if x in taken_positions and y in taken_positions[x]:
                        continue

                    taken_positions[x].append(y)
                    break

                file.write(f"{i + 1}: ({x},{y})\n")

            file.write("Edges:\n")

            # Used to keep track of what edges are already created so we can re=roll the nodes
            edges = {}

            # So that we have a mix of completable nodes and non-completable graphs we use 1.5 * nodes number of edges, number is rather arbitrary besides empirical testing showing that we get a good number of both solvable and unsolvable graphs with this number
            for i in range(floor(1.5 * nodes)):
                node_1 = 0
                node_2 = 0
                count = 0

                # generate nodes until we get a new one that we haven't already used
                while True:
                    node_1 = floor(random.random() * nodes) + 1
                    node_2 = floor(random.random() * nodes) + 1

                    # if we have had a lot of attempts, just quit to keep things pretty speedy. Only a concern on really small graphs with few edge possibilities
                    if count == 1000:
                        break

                    # make sure edges travel to other nodes + make sure they are unique
                    if node_1 == node_2 \
                        or (node_1 in edges and edges[node_1] == node_2) \
                        or (node_2 in edges and edges[node_2] == node_1):
                        count += 1
                        continue

                    # give the new edge a code and reocrd it
                    cost = max(floor(random.random() * nodes), 1) # so that every cost is at least 1
                    edges[node_1] = node_2
                    file.write(f"({node_1},{node_2}): {cost}\n")
                    break

            # generate an origin somewhere in the graph
            file.write("Origin:\n")
            origin_node = floor(random.random() * nodes) + 1 # plus 1 because nodes are 1 based
            file.write(f"{origin_node}\n")

            # Generate destinations
            file.write("Destinations:\n")
            destination_count = min(floor(random.random() * nodes), nodes - 1) # nodes - 1 because an origin shouldn't be a destination
            destinations = set() # keeps track of already assigned destinations
            # this is to check if destinations attempts have failed a nodes number of times
            # at that point we will just loop through all nodes until we have enough destinations
            attempts = 0
            while True:
                # ensure that a destination is an actually possible node
                destination = floor(random.random() * nodes) + 1

                if destination in destinations or destination == origin_node:
                    attempts += 1
                    # prevents edge case of infinite attempts, mostly a problem for smaller graphs
                    if attempts == nodes:
                        break
                    continue
                
                if len(destinations) == 0:
                    file.write(f"{destination}")
                else:
                    file.write(f"; {destination}")

                destinations.add(destination)

                # if we have enough destinations just stop
                if len(destinations) >= destination_count:
                    break

            # add more nodes from the start to feel out remaining destination count in case we had to leave the above loop early
            if len(destinations) < destination_count:
                # So that the next number isn't concatenated to the previous number
                file.write("; ")
                for i in range(1, nodes + 1):
                    if i not in destinations and i != origin_node:
                        file.write(f"{i}; ")
                        destinations.add(i)
                    if destination_count == len(destinations):
                        break

            file.write("\n")
            

# Only have this code run if this code is directly called
if __name__ == "__main__":
    write_tests()
