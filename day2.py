f = open ('input.txt', 'r')
contents = f.read().split('\n')
current_horizontal = 0
current_vertical = 0
for line in contents: 
  if len(line) == 0:
    continue
  direction, amount = line.split(' ')
  if direction == 'forward':
    current_horizontal = current_horizontal + int(amount)
  elif direction == 'up':
    current_vertical = current_vertical - int(amount)
  elif direction == 'down':
    current_vertical = current_vertical + int(amount)

print (current_horizontal * current_vertical)
