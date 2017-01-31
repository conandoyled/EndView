import itertools
import copy

outfile = open("nodups.txt",'w')
sample = open("sample.txt",'w')
size = 6
perms = []
for i in itertools.permutations("ABCDEF"):
  perms.append(list(i))
board = [['A'],['B'],['C'],['D'],['E'],['F']]
boards = [board]
while len(boards[0][0]) != size:
  newboards = []
  for b in boards:
    for p in perms:
      add = True
      row = 0
      while add and row < 6:
        if p[row] in b[row]:
          add = False
        row += 1
      if add:
        new = copy.deepcopy(b)
        for i in range(len(p)):
          new[i].append(p[i])
        newboards.append(new)
  boards = copy.deepcopy(newboards)
  print(len(boards))
boardclues = []
for b in boards:
  board = []
  top = []
  bottom = []
  for i in range(len(b)):
    top.append(b[i][0])
    bottom.append(b[i][size-1])
  board.append(top)
  board.append(bottom)
  board.append(b[0])
  board.append(b[size-1])
  boardclues.append(board)
count = 0
bcount = 0
while len(boardclues) > 0:
  if boardclues.count(boardclues[0]) == 1:
      print(boardclues[0])
      for row in boardclues[0]:
        print(row, file = outfile)
      print(file = outfile)
      count += 1
  elif bcount%1000 == 0:
    for row in boardclues[0]:
      print(row, file = sample)
    print(file = sample)
    print(bcount)
  bcount += 1
  boardclues[:] = [x for x in boardclues if x != boardclues[0]]
print(bcount)
print(count)
print(count, file = outfile)
print(bcount, file = sample)

outfile.close()
sample.close()
