f = ['MMMSXXMASM','MSAMXMSMSA','AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSASXSS','SAXAMASAAA','MAMMMXMMMM','MXMXAXMASX']
f = open('4.txt').read().split('\n')

w = len(f)
p1 = 0
p2 = 0
for r in range(w):
    for c in range(w):
        # horizontal
        if c+3<w and f[r][c] == 'X' and f[r][c+1] == 'M' and f[r][c+2] == 'A' and f[r][c+3] == 'S':
            p1 += 1
        if c+3<w and f[r][c] == 'S' and f[r][c+1] == 'A' and f[r][c+2] == 'M' and f[r][c+3] == 'X':
            p1 += 1
        # vertical
        if r+3<w and f[r][c] == 'X' and f[r+1][c] == 'M' and f[r+2][c] == 'A' and f[r+3][c] == 'S':
            p1 += 1
        if r+3<w and f[r][c] == 'S' and f[r+1][c] == 'A' and f[r+2][c] == 'M' and f[r+3][c] == 'X':
            p1 += 1
        # diagonal right
        if r+3<w and c+3<w and f[r][c] == 'X' and f[r+1][c+1] == 'M' and f[r+2][c+2] == 'A' and f[r+3][c+3] == 'S':
            p1 += 1
        if r+3<w and c+3<w and f[r][c] == 'S' and f[r+1][c+1] == 'A' and f[r+2][c+2] == 'M' and f[r+3][c+3] == 'X':
            p1 += 1
        # diagonal left
        if r+3<w and c-3>=0 and f[r][c] == 'X' and f[r+1][c-1] == 'M' and f[r+2][c-2] == 'A' and f[r+3][c-3] == 'S':
            p1 += 1
        if r+3<w and c-3>=0 and f[r][c] == 'S' and f[r+1][c-1] == 'A' and f[r+2][c-2] == 'M' and f[r+3][c-3] == 'X':
            p1 += 1


        # all answers have 'A' in the middle
        # don't check edges
        if f[r][c] == 'A' and r != 0 and r != w-1 and c != 0 and c != w-1:
            if f[r-1][c-1] == 'M' and f[r+1][c+1] == 'S' and f[r+1][c-1] == 'M' and f[r-1][c+1] == 'S' :
                p2 += 1
            if f[r-1][c-1] == 'M' and f[r+1][c+1] == 'S' and f[r+1][c-1] == 'S' and f[r-1][c+1] == 'M' :
                p2 += 1
            if f[r-1][c-1] == 'S' and f[r+1][c+1] == 'M' and f[r+1][c-1] == 'M' and f[r-1][c+1] == 'S' :
                p2 += 1
            if f[r-1][c-1] == 'S' and f[r+1][c+1] == 'M' and f[r+1][c-1] == 'S' and f[r-1][c+1] == 'M' :
                p2 += 1
print(p1)
print(p2)
