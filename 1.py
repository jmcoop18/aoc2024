f = open('1.txt').read().split('\n')
left = []
right = []
for line in f:
    l,r = line.split('   ')
    l,r = int(l), int(r)
    left.append(l)
    right.append(r)
left = sorted(left)
right = sorted(right)

t = 0
for l,r in zip(left, right):
    t += abs(l - r)
print(t)

t = 0
for n in left:
    t += n * right.count(n)
print(t)