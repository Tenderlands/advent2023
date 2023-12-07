from aocd import get_data
lines = get_data(day=6, year=2023).split('\n')
print(lines)
times = list(map(int,lines[0].split()[1:]))
records = list(map(int,lines[1].split()[1:]))

winning_numbers = []
for i in range(0, len(times)):
    time = times[i]
    rec = records[i]
    min=-1
    max=-1
    #get minimum charge
    for j in range(0, time):
        if j*(time-j) > rec:
            min = j
            break
    #get maximum charge
    for j in reversed(range(0, time)):
        if j*(time-j) > rec:
            max = j
            break
    #determine the number of ways and record ways
    if min!= -1 and max != -1:
        print(f'Race {i}: min:{min} max:{max}')
        winning_numbers.append(max - min + 1)
total = 1
for num in winning_numbers:
    total *= num

print(total)
