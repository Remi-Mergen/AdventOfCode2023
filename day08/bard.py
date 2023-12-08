import re


def parse_network(network_def: str) -> dict[str, list[str]]:
    nodes: dict[str, list[str]] = {}
    for line in network_def.splitlines():
        if line.startswith('AAA ='):
            node_name: str
            connections_list: list[str]

            # Extract node name and connections list
            match = re.match(r'AAA = (.+) = (.+)$', line)
            node_name = match.group(1)
            connections_list = match.group(2).split(',')

            # Add node and connections to the dictionary
            for connection in connections_list:
                if connection not in nodes:
                    nodes[connection] = []

            # Add node connections
            nodes[node_name].append(connections_list[0])
            nodes[node_name].append(connections_list[1])
    return nodes

def traverse_network(start_node: str, instructions: str) -> int:
    visited_nodes: Set[str] = {start_node}
    current_node: str = start_node
    steps: int = 0

    while current_node != 'ZZZ':
        for instruction in instructions:
            if instruction == 'L':
                next_node = nodes[current_node][0]
            elif instruction == 'R':
                next_node = nodes[current_node][1]
            else:
                raise ValueError(f'Invalid instruction: {instruction}')

            if next_node in visited_nodes:
                # Repeat instructions
                instructions += instructions
                continue

            current_node = next_node
            visited_nodes.add(current_node)
            steps += 1

            if current_node == start_node:
                return -1

    return steps

with open('input.txt', 'r') as f:
    network_def = f.read().splitlines()
    instructions = network_def[0]

    steps = traverse_network('AAA', instructions)
    print(steps)
