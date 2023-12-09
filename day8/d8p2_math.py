from aocd import get_data
from math import gcd

directions, nodeList = get_data(day=8, year=2023).split('\n\n')
directions = [*directions]
nodeList = nodeList.split('\n')

nodeMap = {}
positions = []

for node in nodeList:
    curr_node, tup = node.split(' = ')
    l, r = tup.replace('(', '').replace(')', '').split(', ')
    nodeMap[curr_node] = {'L': l, 'R': r}
    if curr_node.endswith('A'):
        positions.append(curr_node)

cycles = []
for current in positions:
    cycle = []
    step_count = 0
    current_steps = directions
    first_z = None

    while True:
        while step_count == 0 or not current.endswith('Z') :
            step_count += 1
            current = nodeMap[current][current_steps[0]]
            current_steps = current_steps[1:] + [current_steps[0]]

        cycle.append(step_count)

        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break
        cycles.append(cycle)
nums = [cycle[0] for cycle in cycles]
#first cycle == each cycle after that

lcm = 1
for num in nums:
    lcm = int(lcm * num / gcd(lcm, num))
print(lcm)
