def init_array():
  return [0,0,0,0,0]

f = open ('input.txt', 'r')
contents = f.read().split('\n')
numbers = [int(i) for i in contents[0].split(',')]
row_counts = []
column_counts = []
contents.pop(0)
all_boards = []
line_index = 0
board_index = 0
board = []
sums = [0]
losers = [0]

for l in contents:
    if len(l) == 0:
        continue
    array = [int(i) for i in [x.strip() for x in l.split(' ') if x.strip()]]
    #array = [x.strip() for x in l.split(' ') if x.strip()]
    sums[board_index] = sums[board_index] + sum(array)
    board.append(array)
    line_index = line_index  + 1
    if line_index == 5:
        all_boards.append(board.copy())
        board_index = board_index + 1
        board.clear()
        sums.append(0)
        line_index = 0
        row_counts.append(init_array())
        column_counts.append(init_array())
        losers.append(board_index)


winning_number = None
winners = []
for n in numbers:
    for b, board in enumerate(all_boards):
        if b in winners:
            continue
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                #print (n, val)
                if n == val:
                    sums[b] = sums[b] - n
                    row_counts[b][r] = row_counts[b][r] + 1
                    column_counts[b][c] = column_counts[b][c] + 1                    
                    if row_counts[b][r] == 5 or column_counts[b][c] == 5:
                        winners.append(b)
                        winner = b
                        winning_number = n

print (winning_number * sums[winner])

