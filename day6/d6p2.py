import re

from aocd import get_data

lines = get_data(day=6, year=2023).split('\n')
time = int(re.sub(' ', '', lines[0].split(':')[1:][0]))
rec = int(re.sub(' ', '', lines[1].split(':')[1:][0]))

minimum = -1
maximum = -1
# get minimum charge
for j in range(0, time):
    if j * (time - j) > rec:
        minimum = j
        break
# get maximum charge
for j in reversed(range(0, time)):
    if j * (time - j) > rec:
        maximum = j
        break
# determine the number of ways and record ways
if minimum != -1 and maximum != -1:
    print(f'Race: min:{minimum} max:{maximum}')
    print(f'There are {maximum - minimum + 1} ways to beat the race')
