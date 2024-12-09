t = 0

def canEval(target, numbers):
    if len(numbers) == 1: return target == numbers[0]

f = open('7.txt').read().split('\n')
for line in f:
    t, n = line.split(': ')
    tgt = int(t)
    nums = [int(x) for x in n.split()]
    if canEval(tgt, nums):
        t += tgt

print(t)