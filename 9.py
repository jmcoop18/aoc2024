test = '2333133121414131402'
s = open('9.txt').read().strip()

disk = []
fid = 0

for i, f in enumerate(s):
    if i % 2 == 0:
        disk += [fid] * int(f)
        fid += 1
    else:
        disk += ['.'] * int(f)

blanks = [i for i,f in enumerate(disk) if f == '.'] 

for i in blanks:
    while disk[-1] == '.': disk.pop()
    if len(disk) <= i: break
    disk[i] = disk.pop()

print(sum(i * x for i, x in enumerate(disk)))
