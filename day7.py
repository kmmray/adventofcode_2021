f = open ('input.txt', 'r')
input = f.read().split('\n')[0].split(',')
positions = [int(i) for i in input]
minimum = None
minimum_position = None
for p in range(min(positions), max(positions)+1):
    running_total = 0
    for calc_p in positions:
        running_total = running_total + abs(p - calc_p)
        if minimum and running_total > minimum:
            continue
    if not minimum or minimum > running_total:
        minimum = running_total
        minimum_position = p

print (minimum, minimum_position)
