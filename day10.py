pts = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
opens = ['(', '[', '{', '<']

closes = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def parse_line(line):
    running_str = ''
    for c in line:
        if running_str == '':
            if ((c == ')' or c == ']' or c == ']' or c == '>')):
                #print (line, running_str)
                return pts[c]
            running_str += c
        else:
            if c in opens:
                running_str += c
            else:
                if closes[running_str[-1]] == c:
                    running_str = running_str[:len(running_str) - 1]

                else:
                    #print (line, running_str)
                    return pts[c]
    return 0

f = open ('input.txt', 'r')
contents = f.read().split('\n')
if contents[-1] == '':
    contents.pop()

total = 0
for line in contents:
    total += parse_line(line)

print (total)
