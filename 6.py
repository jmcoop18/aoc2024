grid = list(map(list, open('6.txt').read().strip().splitlines()))

def loops(r,c):
    nr, nc = -1, 0
    seen = set()

    while True:
        seen.add((r,c,nr,nc))
        if r + nr < 0 or c + nc < 0 or r + nr >= len(grid) or c + nc >= len(grid): return False
        if grid[r + nr][c + nc] == '#':
            nr, nc = nc, -nr
        else:
            r += nr
            c += nc
        if (r, c,nr,nc) in seen:
            return True

# find starting pos ^
for row in range(len(grid)):
    for col in range (len(grid)):
        if grid[row][col] == '^':
            sr, sc = row, col
            break
 
t = 0
for r in range(len(grid)):
    for c in range(len(grid)):
        if grid[r][c] == '.': 
            grid[r][c] = '#'
            if loops(sr,sc): 
                t += 1
            grid[r][c] = '.'

print(t)