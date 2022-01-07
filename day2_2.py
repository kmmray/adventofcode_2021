f = open ('input.txt', 'r')
contents = f.read().split('\n')
horizontal = 0
depth = 0
aim = 0
for line in contents: 
  if len(line) == 0:
    continue
  vals = line.split(' ')
  direction = vals[0]
  amount = int(vals[1]) 
  if direction == 'forward':
    horizontal = horizontal + amount
    depth = depth + aim * amount
  elif direction == 'up':
    aim = aim - amount
  elif direction == 'down':
    aim = aim + amount
print (horizontal * depth)
