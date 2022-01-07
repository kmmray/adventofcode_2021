f = open ('input.txt', 'r')
contents = f.read().split('\n')
value_1 = int(contents[0])
value_3 = int(contents[2])
last_sum = value_1 + int(contents[1]) + value_3 
count = 0
for index, line in enumerate(contents): 
  if index <= 2 or len(line) == 0:
    continue
  current = int(line)
  current_sum = last_sum - value_1 + current
  if current_sum > last_sum:
    count = count + 1
  value_1 = last_sum - value_1 - value_3 
  value_3 = current
  last_sum = current_sum

print (count)
