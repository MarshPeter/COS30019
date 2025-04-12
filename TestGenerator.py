from math import floor
from collections import defaultdict
import random
write_file = "./tests.txt"

count = 0
tests = 12

with open(write_file, "w") as file:
    for i in range(tests):
        nodes = max(floor(random.random() * 15) + 1, 10)
        taken_positions = defaultdict(list)

        file.write("Nodes:\n")

        for i in range(nodes):
            x = 0
            y = 0

            while True:
                x = floor(random.random() * nodes * 2)
                y = floor(random.random() * nodes * 2)
                if x in taken_positions and y in taken_positions[x]:
                    continue

                taken_positions[x].append(y)
                break

            file.write(f"{i + 1}: ({x},{y})\n")

        file.write("Edges:\n")

        edges = {}

        for i in range(floor(1.5 * nodes)):
            node_1 = 0
            node_2 = 0
            count = 0

            while True:
                node_1 = floor(random.random() * nodes) + 1
                node_2 = floor(random.random() * nodes) + 1

                if count == 1000:
                    break

                if node_1 == node_2 \
                    or (node_1 in edges and edges[node_1] == node_2) \
                    or (node_2 in edges and edges[node_2] == node_1):
                    count += 1
                    continue

                cost = max(floor(random.random() * nodes), 1) # so that every cost is at least 1
                edges[node_1] = node_2
                file.write(f"({node_1},{node_2}): {cost}\n")
                break

        file.write("Origin:\n")
        origin_node = floor(random.random() * nodes) + 1
        file.write(f"{origin_node}\n")

        file.write("Destinations:\n")
        destination_count = min(floor(random.random() * nodes), nodes - 1)
        destinations = set()
        # this is to check if destinations attempts have failed a nodes number of times
        # at that point we will just loop through all nodes until we have enough destinations
        attempts = 0
        while True:
            # ensure that a destination is an actually possible node
            destination = floor(random.random() * nodes) + 1


            if destination in destinations or destination == origin_node:
                attempts += 1
                # prevents edge case of infinite attempts
                if attempts == nodes:
                    break
                continue
            
            if len(destinations) == 0:
                file.write(f"{destination}")
            else:
                file.write(f"; {destination}")
            destinations.add(destination)

            if len(destinations) >= destination_count:
                break

        # add more nodes from the start
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
    