def process_point(x, y, basin):
    processed[x][y] = 1
    basin.append([x,y])
    if x != 0 and processed[x-1][y] == 0 and heights[x-1][y] != 9:
        basin = process_point(x-1, y, basin)
    if x != len(heights) - 1 and processed[x+1][y] == 0 and heights[x+1][y] != 9:
        basin = process_point(x+1, y, basin)
    if y != 0 and processed[x][y-1] == 0 and heights[x][y-1] != 9:
        basin = process_point(x, y-1, basin)
    if y != len(x_axis) - 1 and processed[x][y+1] == 0 and heights[x][y+1] != 9:
        basin = process_point(x, y+1, basin)
    return basin

f = open ('input.txt', 'r')
contents = f.read().split('\n')
if contents[-1] == '':
    contents.pop()
heights = []
for line in contents:
    heights.append([int(s) for s in line])

basin = []
all_basins = []
processed = [ [0]*len(heights[0]) for _ in range(0, len(heights)+1) ]
mins = 0
for x, x_axis in enumerate(heights):
    for y, y_axis in enumerate(x_axis):
        if heights[x][y] != 9 and processed[x][y] == 0:
            basin = process_point(x, y, basin)
            all_basins.append(basin)
            basin = []
        
lens = [len(a) for a in all_basins]
sorted_lens = sorted(lens, reverse=True)
print (sorted_lens[0] * sorted_lens[1] * sorted_lens[2])



