
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
    #print (x0,y0,x1,y1)
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
    else: #diagonal
        x_dir = 'up'
        y_dir = 'up'
        if x1 < x0:
            x_dir = 'down'
        if y1 < y0:
            y_dir = 'down'
    
        if (x_dir == y_dir):
            start_x = min(x0,x1)
            start_y = min(y0,y1)
            end_x = max(x0,x1) + 1
            #end_y = max(y0,y1) + 1

            for i in range(end_x-start_x):
                s = f'{start_x + i},{start_y + i}'
                print (s)
                if s in existing:
                    multiples.add(s)
                else:
                    existing.add(s)

        else:
            start_x = min(x0,x1)
            start_y = max(y0,y1)
            end_x = max(x0,x1) + 1
            for i in range(end_x-start_x):
                s = f'{start_x + i},{start_y - i}'
                if s in existing:
                    multiples.add(s)
                else:
                    existing.add(s)
    
print (len(multiples))

