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
    transitions[s1] = s2


for i in range(0,10):
    substrings = [start_string[i] + start_string[i+1] for i in range(0, len(start_string) - 1)]
    new_string = ''
    additions = []
    for s in substrings:
        additions.append(transitions.get(s, ''))
    for j in range(0, len(start_string) - 1):
        new_string += (start_string[j] + additions[j])
    new_string += start_string[-1:]
    start_string = new_string

values = dict(Counter(start_string)).values()
#print (Counter(start_string))
print (max(values) - min(values))

    
