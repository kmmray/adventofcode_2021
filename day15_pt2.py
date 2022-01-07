import sys

def get_neighbors(node):
    connections = []
    for outnode in nodes:
        if graph[node].get(outnode, False) != False:
            connections.append(outnode)
    return connections

def shortest_path(start_node):
    unvisited = {node: None for node in nodes}
    visited = {}
    current = start_node
    current_distance = 0
    unvisited[current] = current_distance

    while True:
        for neighbor, distance in graph[current].items():
            if neighbor not in unvisited:
                continue
            new_distance = current_distance + distance
            if unvisited[neighbor] is None or unvisited[neighbor] > new_distance:
                unvisited[neighbor] = new_distance
        visited[current] = current_distance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = sorted(candidates, key = lambda x: x[1])[0]

    return visited

def increase_line(input):
    new_line = input
    l = input
    for i in range(0,4):
        new = increases[l]
        new_line += new
        l = new
    return new_line

def process_contents(contents):
    row_count = len(contents) - 1
    column_count = len(contents[0]) - 1
    lines = contents.split('\n')
    lines.pop()
    global increases
    increases = {}
    for i, line in enumerate(lines):
        line_increase = ''
        for c in line:
            if c == '9':
                line_increase += ('1')
            else:
                line_increase += (str(1+int(c)))
        increases[line] = line_increase
     
    next_increases_keys = increases.keys()
    for i in range(0,10):
        next_increases = []
        for increase in next_increases_keys:
            line_increase = ''
            for c in increase:
                if c == '9':
                    line_increase += ('1')
                else:
                    line_increase += (str(1+int(c)))
            increases[increase] = line_increase
            next_increases.append(line_increase)
            next_increases_keys = next_increases
    
    new_lines = []
    for line in lines:
        new_lines.append(increase_line(line))
    for line in lines:
        new_lines.append(increases[line])

    initial_row_count = len(lines)
    for i in range(1,4):
        for lindex in range(initial_row_count * i, initial_row_count * (i+1)):
            new_lines.append(increases[new_lines[lindex]])
    #print (len(lines), len(new_lines))

    for i in range(len(lines), len(new_lines)):
        new_lines[i] = increase_line(new_lines[i])

    return new_lines
    #print (len(new_lines))


f = open ('input.txt', 'r')
contents = process_contents(f.read())
max_x = len(contents[0]) - 1
max_y = len(contents) - 1
#print (contents)
if contents[-1] == '':
    contents.pop()
graph = {}
nodes = {}
flashes = 0
for x, row in enumerate(contents):
    for y, column in enumerate(row):
        graph[f'{x},{y}'] = {}

for x, row in enumerate(contents):
    for y, column in enumerate(row):
        key = f'{x},{y}'
        column_int = int(column)
        nodes[key] = column_int
        if x != max_x:
            graph[f'{x+1},{y}'][key] = column_int
        if x != 0:
            graph[f'{x-1},{y}'][key] = column_int
        if y != max_y:
            graph[f'{x},{y+1}'][key] = column_int
        if y != 0:
            graph[f'{x},{y-1}'][key] = column_int

print (shortest_path('0,0')[f'{len(contents)-1},{len(contents[0])-1}'])
