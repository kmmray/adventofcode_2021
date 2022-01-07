f = open ('input.txt', 'r')
initial_values = f.read().split('\n')[0].split(',')
fish_by_age = [0] * 9
for i in initial_values:
    int_val = int(i)
    fish_by_age[int_val] = fish_by_age[int_val] + 1

for _ in range(0,256):
    new_fish = fish_by_age[0]
    for i in range(1,9):
        fish_by_age[i-1] = fish_by_age[i]
    fish_by_age[8] = new_fish
    fish_by_age[6] = fish_by_age[6] + new_fish
print (sum(fish_by_age))
