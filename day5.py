
import re

f = open ('input.txt', 'r')
contents = f.read().split('\n')
existing = set()
multiples = set()
for l in contents:
    if len(l) == 0:
        continue
    pts = re.sub(r'  ', ',', re.sub(r'>', '', re.sub(r'-', '', l)))
    x0,y0,x1,y1 = [int(i) for i in pts.split(',')]
    print (x0,y0,x1,y1)
    if x0 == x1:
        start = min(y0,y1)
        end = max(y0,y1) + 1
        for y in range(start,end):
            s = f'{x0},{y}'
            if s in existing:
                multiples.add(s)
            else:
                existing.add(s)
    elif y0 == y1:
        start = min(x0,x1)
        end = max(x0,x1) + 1
        for x in range(start,end):
            s = f'{x},{y0}'
            if s in existing:
                multiples.add(s)
            else:
                existing.add(s)

print (len(multiples))

