f = open ('input.txt', 'r')
contents = f.read().split('\n')
if contents[-1] == '':
    contents.pop()
heights = []
for line in contents:
    heights.append([int(s) for s in line])

mins = 0
for x, x_axis in enumerate(heights):
    for y, y_axis in enumerate(x_axis):
        is_min =1
        if heights[x][y] == 9:
            continue
        if x != 0:
            if heights[x][y] >= heights[x-1][y]:
                continue
        if x != len(heights) - 1:
            if heights[x][y] >= heights[x+1][y]:
                continue
        if y != 0:
            if heights[x][y] >= heights[x][y-1]:
                continue
        if y != len(x_axis) - 1:
             if heights[x][y] >= heights[x][y+1]:
                 continue
        mins += heights[x][y]+1
print (mins)