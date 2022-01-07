import sys

def get_neighbors(node):
    connections = []
    for outnode in nodes:
        if graph[node].get(outnode, False) != False:
            connections.append(outnode)
    return connections

def risk(begin, end):
    return graph[begin][end]


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

    #print(visited)
    return visited

f = open ('input.txt', 'r')
contents = f.read().split('\n')
max_x = len(contents[0]) - 1
max_y = len(contents) - 2
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
        #print (graph)
        if x != max_x:
            graph[f'{x+1},{y}'][key] = column_int
        if x != 0:
            graph[f'{x-1},{y}'][key] = column_int
        if y != max_y:
            graph[f'{x},{y+1}'][key] = column_int
        if y != 0:
            graph[f'{x},{y-1}'][key] = column_int

print (shortest_path('0,0')[f'{len(contents)-1},{len(contents[0])-1}'])
