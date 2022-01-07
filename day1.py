f = open ('input.txt', 'r')
contents = f.read().split('\n')
last = int(contents[0])
contents.pop(0)
count = 0
for line in contents:
  if len(line) == 0:
    continue
  current = int(line)
  if current > last:
    count = count + 1
  last = current

print (count)
