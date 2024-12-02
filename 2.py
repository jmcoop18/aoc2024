reports =  [list(map(int, i.split(' '))) for i in open('2.txt').read().splitlines()]

def isGood(list):
    sort = (list==sorted(list)) or list==sorted(list,reverse=True)
    good = False
    if all( 1 <= abs(i-j) <= 3 for i,j in zip(list, list[1:])):
            good = True
    return sort and good

t = 0
for level in reports:
    if isGood(level):
         t += 1
print(t)

t = 0
for level in reports:
     gd = False
     for j in range(len(level)):
          skip = level[:j] + level[j+1:]
          if isGood(skip):
               gd = True
     if gd:
        t += 1
print(t)
