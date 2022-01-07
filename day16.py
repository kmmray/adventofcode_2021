def parse_binary_string(start, end, skip_start=None, skip=None):
    total = 0
    c = 0
    next_skip = None
    if skip_start:
        next_skip = end
        
    for i in range(end, start-1, -1):
        if next_skip and i == next_skip:
            next_skip -= 5
            continue
        total += int(bit_string[i]) * (2 ** c)
        c += 1

    return total

f = open ('input.txt', 'r')
lines = f.read().split('\n')
versions = 0

for value in lines: 
    if len(value) == 0:
        continue
    bit_string = ''
    string_len = len(value) 
    for i in range(0, string_len):
        bit_string += '{0:04b}'.format(int(value[i], 16))
    #print (f'{value}\n{bit_string}')
    #print (f'len = {len(bit_string)}')

    position = 0
    while (position + 7 < len(bit_string)):
        version = int(bit_string[position:position+3], 2)
        versions += version
        packet_type_id = bit_string[position+3:position+6]
        position += 6
        if packet_type_id == '100':
            last_packet = position
            while bit_string[last_packet] != '0':
                last_packet += 5
            literal = parse_binary_string(position, last_packet+5, last_packet, skip=5)
            position = last_packet + 5
        else:
            type_id = bit_string[position]
            position += 1
            if type_id == '0':
                length = int(bit_string[position+7:position+22], 2) #parse_binary_string(start+7, start+21)
                position += 15      
            else:
                length = int(bit_string[position+7:position+18], 2)
                position += 11
        
print (versions)

