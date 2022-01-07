from collections import Counter
f = open ('input.txt', 'r')
contents = f.read().split('\n')
start_string = contents[0]
contents.pop(0)
transitions = {}
for line in contents:
    if len(line) == 0:
        continue
    s1, s2 = line.split(' -> ')
    transitions[s1] = [s1[0] + s2, s2 + s1[1]]
#print (transitions)

current_substrings = [start_string[i] + start_string[i+1] for i in range(0, len(start_string) - 1)]
totals = {}
for s in current_substrings:
    if s not in totals:
        totals[s] = 1
    else:
        totals[s] += 1

#print (totals)

for i in range(0,40):
    add_totals = {}
    keys = totals.keys()
    add_substrings = {}
    for k in keys:
        if k in transitions:
            add_totals[k] = 0
    for k in keys:
        new_strings = transitions[k]
        if totals[k] != 0:
            for x in range(0,2):
                if not new_strings[x] in add_totals:
                    add_totals[new_strings[x]] = totals[k] 
                    #print (f'{x} 1 set {new_strings[x]} {totals[k]}')
                else:
                    add_totals[new_strings[x]] += totals[k]
                    #print (f'{x} 2 add {new_strings[x]} {totals[k]}')

    for k2 in add_totals.keys():
        totals[k2] = add_totals[k2]
    
    #print (totals)

char_totals = {}
for k in totals.keys():
    if k[0] not in char_totals:
        char_totals[k[0]] = totals[k]
    else:
        char_totals[k[0]] += totals[k]

char_totals[start_string[-1:]] += 1
values = dict(Counter(char_totals)).values()
#print (char_totals)
print (max(values) - min(values))       