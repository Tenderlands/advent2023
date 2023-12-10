from aocd import get_data

# import numpy as np
lines = get_data(day=9, year=2023).splitlines()


def predict_next_in_seq(seq):
    new_seq = []
    for i in range(len(seq) - 1):
        new_seq.append(seq[i + 1] - seq[i])
    if any(a != 0 for a in new_seq):
        predicted = predict_next_in_seq(new_seq)
        return seq[-1] + predicted
    else:
        return seq[-1]


total = 0
for line in lines:
    sequence = [int(x) for x in line.split(' ')]
    next_num = predict_next_in_seq(sequence)
    total += next_num
print(total)
