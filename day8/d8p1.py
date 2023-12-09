import sys

from aocd import get_data

directions, nodeList = get_data(day=8, year=2023).split('\n\n')
directions = [*directions]
nodeList = nodeList.split('\n')
nodeMap = {}
for node in nodeList:
    curr_node, tup = node.split(' = ')
    l, r = tup.replace('(', '').replace(')', '').split(', ')
    nodeMap[curr_node] = {'L': l, 'R': r}
sys.setrecursionlimit(100000)
def traverse(step=0, previous='AAA'):
    instruction = directions[step % len(directions)]
    step += 1
    if nodeMap[previous][instruction] == 'ZZZ':
        print(step)
    else:
        previous = nodeMap[previous][instruction]
        traverse(step=step, previous=previous)

traverse()

