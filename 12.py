from collections import deque

grid = open('12.txt').read().strip().splitlines()
size = len(grid)

regions = []
found = set()

for r in range(size):
    for c in range(size):
        if (r,c) in found: continue
        found.add((r,c))
        region = {(r,c)}
        q = deque([(r,c)])
        tgt = grid[r][c]
        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr+1, cc), (cr, cc+1), (cr-1, cc), (cr, cc-1)]:
                if nr < 0 or nc < 0 or nr >= size or nc >= size: continue
                if grid[nr][nc] != tgt: continue
                if (nr,nc) in region: continue
                region.add((nr,nc))
                q.append((nr, nc))
        found |= region
        regions.append(region)

def perimeter(region):
    t = 0
    for (r,c) in region:
        t += 4
        for nr, nc in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
            if (nr,nc) in region:
                t -= 1
    return t

def sides(region):
    possibleCorners = set()
    for (r,c) in region:
        for (nr, nc) in [(r-.5, c-.5), (r+.5, c-.5), (r+.5, c+.5), (r-.5, c+.5)]:
            possibleCorners.add((nr,nc))
    t = 0
    for (cr,cc) in possibleCorners:
        config = [(nr, nc) in region for nr, nc in [(cr-.5, cc-.5), (cr+.5, cc-.5), (cr+.5, cc+.5), (cr-.5, cc+.5)]]
        n = sum(config)
        if n == 1:
            t += 1
        elif n == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                t += 2
        elif n == 3:
            t += 1
    return t

print(sum((len(i) * perimeter(i)) for i in regions))
print(sum((len(i) * sides(i)) for i in regions))