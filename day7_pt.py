import time

def build_sum_lookup(maximum):
    sum_dict = {}
    sum = 0
    for i in range(0,maximum+1):
        sum = sum + i
        sum_dict[i] = sum

    return sum_dict

startTime = time.time()

f = open ('input.txt', 'r')
input = f.read().split('\n')[0].split(',')
positions = [int(i) for i in input]
sum_dict = build_sum_lookup(max(positions))
minimum = None
minimum_position = None
for p in range(min(positions), max(positions)+1):
    running_total = 0
    for calc_p in positions:
        running_total = running_total + sum_dict[abs(p - calc_p)]
        if minimum and running_total > minimum:
            continue
    if not minimum or minimum > running_total:
        minimum = running_total
        minimum_position = p

print (minimum, minimum_position)
print('Execution time in seconds: ' + str(time.time() - startTime))
