from aocd import get_data

lines = get_data(day=9, year=2023).splitlines()


def predict_prev_in_seq(seq):
    new_seq = []
    for i in reversed(range(len(seq) - 1)):
        new_seq.append(seq[i + 1] - seq[i])
    if any(a != 0 for a in new_seq):
        predicted = predict_prev_in_seq(new_seq[::-1])
        return seq[0] - predicted
    else:
        return seq[0]


total = 0
for line in lines:
    sequence = [int(x) for x in line.split(' ')]
    next_num = predict_prev_in_seq(sequence)
    total += next_num
print(total)
