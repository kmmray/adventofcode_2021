f = open ('input.txt', 'r')
contents = f.read().split('\n')
total = 0

lens = [6, 2, 5, 5, 4, 6, 3, 7, 6]
sum_dict = {
    'abcefg':0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}


for l in contents:
    signals = [''] * 7
    length_dict = {}
    for length in range(0, 8):
        length_dict[length] = [] 
    if len(l) == 0:
        continue
    str_total = ''
    signal_s, output_s = l.split('|')
    unsorted_signals = signal_s.split(' ')
    messages = output_s.split(' ')
    messages.pop(0)
    for us in unsorted_signals:
        length_dict[len(us)].append(us)
    
    print (length_dict)
    not_assigned = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    ones, not_ones = [], []
    for st in length_dict[3][0]:
        for c in st:
            if c not in length_dict[2][0]:
                signals[0] = c
                print (f'a0 = {c}')
                not_assigned.remove(c)
                break
    for st in length_dict[4][0]:
        for c in st:
            if c in length_dict[2][0]:
                ones.append(c)
            else:
                not_ones.append(c)
    for st in length_dict[4][0]:
        for c in st:
            if c not in ones:
                if (c not in length_dict[6][0] or c not in length_dict[6][1] or c not in length_dict[6][2]):
                    signals[3] = c #d
                    not_assigned.remove(c)
                    not_ones.remove(c)
                    print (f'd3 = {c}')
                    break
            else:
                if (c not in length_dict[6][0] or c not in length_dict[6][1] or c not in length_dict[6][2]):
                    signals[2] = c #c
                    not_assigned.remove(c)
                    ones.remove(c)
                    print (f'c2 = {c}')
                    break
    
    signals[1] = not_ones[0] #b
    signals[5] = ones[0] #f
    print (f'b1 = {not_ones[0]}')
    print (f'f5 = {ones[0]}')
    not_assigned.remove(not_ones[0])
    not_assigned.remove(ones[0])

    for c in not_assigned: 
        if (c not in length_dict[5][0] or c not in length_dict[5][1] or c not in length_dict[5][2]):
            signals[4] = c #e
            print (f'e4 = {c}')
            not_assigned.remove(c)

    signals[6] = not_assigned[0] #g
    
    letter_mappings = {}
    for i, l in enumerate(signals):
        letter_mappings[l] = chr(i + 97)
    print (letter_mappings)
    line_string = ''
    for m in messages:
        print (f'message = {m}')
        new_s = ''
        for s in m:
            print (s, letter_mappings[s])
            new_s += letter_mappings[s]
        sorted_m = ''.join(sorted(new_s))
        print (new_s, sorted_m)
        line_string += str(sum_dict[sorted_m])
    total += int(line_string)
    print (f'line_string = {line_string}')
print (total)       
        

