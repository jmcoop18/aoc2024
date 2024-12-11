from functools import cache
stones = list(map(int, open('11.txt').read().strip().split(' ')))

@cache
def count(s, b):
        if b == 0:
             return 1
        if s == 0:
            return count(1, b-1)
        dig = len(str(s))
        hp = 10 ** (dig//2)
        if dig % 2 == 0:
            left = s // hp
            right = s % hp 
            return count(left, b-1) + count(right, b-1)
        return count(s*2024, b-1)

print(sum(count(stone, 25) for stone in stones))
print(sum(count(stone, 75) for stone in stones))
