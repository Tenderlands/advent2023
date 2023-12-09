from aocd import get_data

directions, nodeList = get_data(day=8, year=2023).split('\n\n')
directions = [*directions]
nodeList = nodeList.split('\n')
# directions = 'LR'
#
# nodeList = ["11A = (11B, XXX)",
#             "11B = (XXX, 11Z)",
#             "11Z = (11B, XXX)",
#             "22A = (22B, XXX)",
#             "22B = (22C, 22C)",
#             "22C = (22Z, 22Z)",
#             "22Z = (22B, 22B)",
#             "XXX = (XXX, XXX)", ]

nodeMap = {}
current_nodes = []

for node in nodeList:
    curr_node, tup = node.split(' = ')
    l, r = tup.replace('(', '').replace(')', '').split(', ')
    nodeMap[curr_node] = {'L': l, 'R': r}
    if curr_node[2] == 'A':
        current_nodes.append(curr_node)
step = 0
while True:
    instruction = directions[step % len(directions)]
    step += 1
    all_nodes_end = True
    next_nodes = []
    for node in current_nodes:
        all_nodes_end = all_nodes_end and nodeMap[node][instruction][2] == 'Z'
        next_nodes.append(nodeMap[node][instruction])
    if all_nodes_end:
        break
    else:
        current_nodes = next_nodes
    if step % 1000 == 0:
        print(step)
print(step)
