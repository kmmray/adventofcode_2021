f = open ('input.txt', 'r')
contents = f.read().split('\n')
if (contents[len(contents)-1] == ''):
  del(contents[-1])
ones = []
zeros = []
total_values = 0
for c in contents[0]:
  ones.append(0)
  zeros.append(0)
for line in contents: 
  total_values = total_values + 1
  for index, c in enumerate(line):
    if c == '1':
      ones[index] = ones[index] + 1
    else:
      zeros[index] = zeros[index] + 1

og_list = contents
current_ones = ones.copy()
current_zeros = zeros.copy()
current_index = 0
while len(og_list) > 1:
  tmp_list = og_list.copy()
  mcv = str(int(current_ones[current_index] >= current_zeros[current_index]))
  for line in og_list:
    if line[current_index] != mcv:
      tmp_list.remove(line)
      for i, c in enumerate(line):
        if c == '1':
          current_ones[i] = current_ones[i] - 1
        else:
          current_zeros[i] = current_zeros[i] - 1
      if len(tmp_list) == 1:
        break
  current_index = current_index + 1
  og_list = tmp_list.copy()

co2_list = contents
current_ones = ones.copy()
current_zeros = zeros.copy()
current_index = 0
while len(co2_list) > 1:
  tmp_list = co2_list.copy()
  lcv = str(int(current_ones[current_index] < current_zeros[current_index]))
  for line in co2_list:
    if line[current_index] != lcv:
      tmp_list.remove(line)
      for i, c in enumerate(line):
        if c == '1':
          current_ones[i] = current_ones[i] - 1
        else:
          current_zeros[i] = current_zeros[i] - 1
      if len(tmp_list) == 1:
        break
  current_index = current_index + 1
  co2_list = tmp_list.copy()

og = int(og_list[0], 2)
c02 = int(co2_list[0], 2)
print (og * c02)