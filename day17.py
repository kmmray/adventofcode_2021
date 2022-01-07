def x_range(x):
    if (x < start_x):
        return "below"
    elif x > end_x:
        return "above"

    return "in"

def y_range(y):
    if (y < start_y):
        return "below"
    elif y > end_y:
        return "above"

    return "in"

def in_range(x, y):
    return (x >= start_x and x <= end_x and y >= start_y and y <= end_y)

f = open ('input.txt', 'r')
line = f.read().split('\n')[0]

splits = line.split(',')
start_x = int(splits[0].split('..')[0].strip('x='))
end_x = int(splits[0].split('..')[1].strip())
start_y = int(splits[1].split('..')[0].strip(' y='))
end_y = int(splits[1].split('..')[1].strip())

print (start_x, end_x, start_y, end_y)

if start_x >= 0:
    x_dir = 1
    x_stop = start_x + 1
    initial_x = "below"
else:
    x_dir = -1
    x_stop = end_x - 1
    initial_x = "above"

if start_y >= 0:
    y_dir = 1
    y_stop = start_y + 1
    initial_y = "below"
else:
    y_dir = -1
    y_stop = end_y - 1
    initial_y = "above"

global_max_y = -100000
print (start_y, y_dir)
for x in range(0, start_x, x_dir):
    for y in range(0, start_y, y_dir):
        hit_target = False
        print (f'point {x},{y}')
        new_x = x
        new_y = y
        max_y = -100000
        while True:
            new_x = new_x + new_x + x_dir
            new_y = new_y + new_y - 1
            #print (f'new_x = {new_x}, new_y = {new_y}, max_y = {max_y}')
            if in_range(x, y):
                hit_target = True
            print (new_x, new_y, hit_target)
            max_y = max(max_y, new_y)
            if (x_range(new_x) != initial_x and y_range(new_y) != initial_y):
                print (f'break {new_x} {new_y} {initial_x} {initial_y}')
                break
        if hit_target:
            global_max_y = max(global_max_y, max_y)
            

print(global_max_y)


