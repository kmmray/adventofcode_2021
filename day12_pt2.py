from collections import Counter
def traverse_from_point(start_pt, used=[]):
    path_count = 0
    if start_pt == 'end':
        return 1
    if start_pt.islower():
        used.append(start_pt)
    for p in rules[start_pt]:
        if len(used) <= len(Counter(used).keys()) + 1:
            path_count += traverse_from_point(p, used.copy())

    return path_count 
    
f = open ('input.txt', 'r')
contents = f.read().split('\n')
if contents[-1] == '':
    contents.pop()

rules = dict()
for l in contents:
    pt1, pt2 = l.split('-')
    if pt1 not in rules:
        rules[pt1] = [] 
    if pt2 not in rules:
        rules[pt2] = [] 
    if pt1 != 'start':
        rules[pt2].append(pt1)
    if pt2 != 'start':
        rules[pt1].append(pt2)
    
rules.pop('end')
        
#print (rules)
total_paths = traverse_from_point(start_pt='start')

print (total_paths)


