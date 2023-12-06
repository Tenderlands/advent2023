import numpy as np

ignore_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

with open('d3p1input.txt', 'r') as file:
    lines = file.readlines()
array = [list(line.strip()) for line in lines]
height = len(array)
width = len(array[0])

include = np.zeros((width, height), dtype=bool)
for i in range(0, height):
    for j in range(0, width):
        if array[i][j] not in ignore_list:
            include[max(i - 1, 0)][max(j - 1, 0)] = True
            include[max(i - 1, 0)][j] = True
            include[max(i - 1, 0)][min(j + 1, width-1)] = True
            include[i][max(j - 1, 0)] = True
            include[i][j] = True
            include[i][min(j + 1, width-1)] = True
            include[min(i + 1, height-1)][max(j - 1, 0)] = True
            include[min(i + 1, height-1)][j] = True
            include[min(i + 1, height-1)][min(j + 1, width)] = True

total = 0
num = ""
valid = False

for i in range(0, height):
    for j in range(0, width):
        if array[i][j] in ignore_list and array[i][j] != '.':
            num += array[i][j]
            valid = include[i][j] or valid
        else:
            if num != "" and valid:
                total += int(num)
                num = ""
                valid = False
            elif num != "" and not valid:
                num = ""
    if num != "" and valid:
        total += int(num)
        num = ""
        valid = False

print(total)
