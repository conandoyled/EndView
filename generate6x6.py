import itertools
import copy

perms = []
for i in itertools.permutations("ABCDEF"):
  perms.append(list(i))
board = [['A'],['B'],['C'], ['D'], ['E'], ['F']]
boards = [board]
while len(boards[0][0]) != 6:
  newboards = []
  for b in boards:
    for p in perms:
      add = True
      for row in range(len(b)):
        if p[row] in b[row]:
          add = False
      if add:
        new = copy.deepcopy(b)
        for i in range(len(p)):
          new[i].append(p[i])
        newboards.append(new)
  boards = copy.deepcopy(newboards)
  print(len(boards))
      
##import random
##lst = [10001]
##for i in range(1000000):
##  num = random.randint(0,10000)
##  lst.append(num)
##print("Done")
###lst.sort()
##print("Done")
##for l in lst:
##  if lst.count(l) == 1:
##    print(l)
##print("Done")
