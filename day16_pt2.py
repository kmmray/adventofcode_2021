import numpy

def parse_literal(start):
    last_packet = start
    while bit_string[last_packet] != '0':
        last_packet += 5
    total = 0
    c = 0
    next_skip = last_packet + 5 
    for i in range(last_packet + 5, start-1, -1):
        if i == next_skip:
            next_skip -= 5
            continue
        total += int(bit_string[i]) * (2 ** c)
        c += 1

    return last_packet+5, total

def parse_headers(start):
    version = int(bit_string[start: start+3], 2) 
    packet_type_id = int(bit_string[start+3: start+6], 2) 
    type_id = int(bit_string[start+6: start+7], 2) 
    return version, packet_type_id, type_id

def process_packet(start, operator):
    packet_values = []
    position = start
    version, packet_type_id, type_id = parse_headers(start)
    position += 6

    if packet_type_id == 4:
        position, literal = parse_literal(position)
        packet_values.append(literal)
    else:
        position += 1
        if type_id == 0:
            length = int(bit_string[position:position+15], 2) 
            position += 15      
            current = position
            while position < current + length:            
                position, value = process_packet(position, packet_type_id)
                packet_values.append(value)

        else:
            length = int(bit_string[position:position+11], 2)
            position += 11
            for _ in range(0, length):
                position, value = process_packet(position, packet_type_id)
                packet_values.append(value)
    return position, calculate_values(packet_type_id, packet_values)

def calculate_values(packet_type_id, values):
    #print (packet_type_id, values)
    if packet_type_id == 0:
        return sum(values)
    if packet_type_id == 1:
        return numpy.prod(values)
    if packet_type_id == 2:
        return min(values)
    if packet_type_id == 3:
        return max(values)
    if packet_type_id == 4:
        return values[0] 
    if packet_type_id == 5:
        return 1 if values[0] > values[1] else 0
    if packet_type_id == 6:
        return 1 if values[0] < values[1] else 0
    if packet_type_id == 7:
        return 1 if values[0] == values[1] else 0

f = open ('input.txt', 'r')
lines = f.read().split('\n')
versions = 0
packet_total = 0

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
        position, value = process_packet(position, None)
        print (value)
        
