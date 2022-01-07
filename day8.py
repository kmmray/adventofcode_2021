f = open ('input.txt', 'r')
contents = f.read().split('\n')
found_lengths = 0
for l in contents:
    if len(l) == 0:
        continue
    signal_s, output_s = l.split('|')
    output = output_s.split(' ')
    for o in output:
        if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
            found_lengths += 1

print (found_lengths)       
        

