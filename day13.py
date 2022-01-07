import numpy
f = open ('input.txt', 'r')
contents = f.read().split('\n')
if contents[0] == ' ':
    contents.pop(0)
X = 0
Y = 1
pts = []
folds = []
parse = 'pts'
max_x = 0
max_y = 0
for line in contents:
    if parse == 'pts':
        if line == '':
            parse = 'folds'
            continue
        pt = line.split(',')
        pts.append([int(pt[0]), int(pt[1])])
        max_x = max(int(pt[0]), max_x)
        max_y = max(int(pt[1]), max_y)
        
    if parse == 'folds' and not line == '':
        f = line.split(' ')[2].split('=')
        folds.append([f[0], int(f[1])])
cur_fold = folds[0]
val = cur_fold[1]
#print (pts)
end = val-1
removal = []
new_pts = []
if cur_fold[0] == 'y':
    start = (max_y//2)- val
    for p in pts:
        if p[Y] > val:
            #print ('current {} adding {} {}'.format (p, p[X], p[Y]-2 * (p[Y]-val)))
            new_pts.append([p[X], p[Y]-2 * (p[Y]-val)])
        if p[Y] >= val:
            removal.append(p)
else:
    start = (max_x//2)- val
    for p in pts:
        if p[X] > val:
            #print ('current {} adding {} {}'.format (p, p[X]-2 * (p[X]-val), p[Y]))
            new_pts.append([p[X]-2 * (p[X]-val), p[Y]])
        if p[X] >= val:
            removal.append(p)

for i in removal:
    pts.remove(i)
pts.extend(new_pts)


print (len(numpy.unique(pts, axis=0)))


a = [[0 * 50] * 50]
s = ''
for i in range(0, 50):
    for j in range (0, 50):
        if [i,j] in pts:
            s += '#'
        else:
            s += '.'
    s += '\n'

#print (s)




