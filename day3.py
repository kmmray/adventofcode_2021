f = open ('input.txt', 'r')
contents = f.read().split('\n')
current_ones= []
total_values = 0
for c in contents[0]:
  current_ones.append(0)
for line in contents: 
  if len(line) == 0:
    continue
  total_values = total_values + 1
  for index, c in enumerate(line):
    if c == '1':
      current_ones[index] = current_ones[index] + 1

half = total_values/2
gamma, epsilon = "", ""
for v in current_ones:
  if v >= half:
    gamma = gamma +'1'
    epsilon = epsilon + '0'
  else:
    gamma = gamma +'0'
    epsilon = epsilon + '1'

bin_gamma = int(gamma, 2)
bin_epsilon = int(epsilon, 2)
print (bin_gamma * bin_epsilon)