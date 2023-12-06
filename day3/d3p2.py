import numpy as np

ignore_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

with open('d3p1input.txt', 'r') as file:
    lines = file.readlines()
array = [list(line.strip()) for line in lines]
height = len(array)
width = len(array[0])

number_mask = np.zeros((width, height), dtype=int)

number = 1
num_dict = {}
for i in range(0, height):
    for j in range(0, width):
        if array[i][j] in ignore_list and array[i][j] != '.':
            if (j - 1 < 0) or number_mask[i][j - 1] == 0:
                number_mask[i][j] = number
                num_dict[str(number)] = str(array[i][j])
                number += 1
            else:
                number_mask[i][j] = number_mask[i][j - 1]
                num_dict[str(number - 1)] += str(array[i][j])
np_array = np.array(array)
x, y = np.where(np_array == "*")

total = 0
for i in range(0, len(x)):
    num_set = set()
    num_set.add(str(number_mask[max(x[i] - 1, 0)][max(y[i] - 1, 0)]))
    num_set.add(str(number_mask[max(x[i] - 1, 0)][y[i]]))
    num_set.add(str(number_mask[max(x[i] - 1, 0)][min(y[i] + 1, width-1)]))
    num_set.add(str(number_mask[x[i]][max(y[i] - 1, 0)]))
    num_set.add(str(number_mask[x[i]][min(y[i] + 1, width - 1)]))
    num_set.add(str(number_mask[min(x[i] + 1, height-1)][max(y[i] - 1, 0)]))
    num_set.add(str(number_mask[min(x[i] + 1, height-1)][y[i]]))
    num_set.add(str(number_mask[min(x[i] + 1, height-1)][min(y[i] + 1, width-1)]))

    num_set.remove('0')
    if len(num_set) == 2:
        add= 1
        for num in num_set:
            add *= int(num_dict[str(num)])
        total += add
print(total)