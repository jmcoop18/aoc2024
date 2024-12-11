grid = open('8.txt').read().strip().splitlines()
antidotes = [[0]*len(grid[0]) for _ in grid]
antennas = []

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != '.':
            antennas.append((grid[r][c], (r, c)))

print(sorted(antennas))

def slope(r1, c1, r2, c2):
    return (r2-r1)/(c2-c1)


