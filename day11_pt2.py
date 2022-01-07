import numpy

def process_point(x, y, levels):
    if (levels[x][y] > 9) and flash_array[x][y] == 0:
        flash_array[x][y] = 1
        is_x_start = x == 0
        is_y_start = y == 0
        is_x_end = x == len(levels) - 1
        is_y_end = y == len(levels[0]) - 1

        if not is_x_start:
            levels[x-1][y] += 1
            levels = process_point(x-1, y, levels)
        if not is_x_end:
            levels[x+1][y] += 1
            levels = process_point(x+1, y, levels)
        if not is_y_start:
            levels[x][y-1] += 1
            levels = process_point(x, y-1, levels)
        if not is_y_end:
            levels[x][y+1] += 1
            levels = process_point(x, y+1, levels)

        # Diagonals
        if not is_x_start and not is_y_start:
            levels[x-1][y-1] += 1
            levels = process_point(x-1, y-1, levels)
        if not is_x_start and not is_y_end:
            levels[x-1][y+1] += 1
            levels = process_point(x-1, y+1, levels)
        if not is_x_end and not is_y_end:
            levels[x+1][y+1] += 1
            levels = process_point(x+1, y+1, levels)
        if not is_x_end and not is_y_start:
            levels[x+1][y-1] += 1
            levels = process_point(x+1, y-1, levels)
 
    return levels

f = open ('input.txt', 'r')
contents = f.read().split('\n')
if contents[-1] == '':
    contents.pop()
l = []
flashes = 0
for line in contents:
    l.append([int(s) for s in line])
levels = numpy.array(l)
for i in range(0,1000):
    flash_array = [[0]*len(levels[0]) for _ in range(0, len(levels)) ]
    levels = levels + 1
    for x, x_axis in enumerate(levels):
        for y, y_axis in enumerate(x_axis): 
            levels = process_point(x, y, levels)

    flashes = 0
    for x, a in enumerate(levels):
        for y, y_axis in enumerate(x_axis):
            if levels[x][y] > 9:
                levels[x][y] = 0
                flashes += 1
    #print (f'i={i}, {levels}')
    if flashes == len(l) * len(l[0]):
        print (i+1)
        exit(0)
