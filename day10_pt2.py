import numpy

pts = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}
closes = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

opens = ['(', '[', '{', '<']

def parse_line(line):
    running_str = ''
    for c in line:
        if running_str == '':
            if ((c == ')' or c == ']' or c == ']' or c == '>')):
                return 0
            running_str += c
        else:
            if c in opens:
                running_str += c
            else:
                if closes[running_str[-1]] == c:
                    running_str = running_str[:len(running_str) - 1]
                else:
                    return 0
    
    total = 0
    for c in reversed(running_str):
        total = (total * 5) + pts[c]
    #print (running_str)
    return total

f = open ('input.txt', 'r')
contents = f.read().split('\n')
if contents[-1] == '':
    contents.pop()
chunks = []
total = 0

totals = []
for line in contents:
    total = parse_line(line)
    if total != 0: 
        totals.append(total)

print (numpy.median(sorted(totals)))
