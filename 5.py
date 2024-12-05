from collections import defaultdict
rules, pages = open('5.txt').read().strip().split('\n\n')
rules = [[int(k) for k in j] for j in [i.split('|') for i in rules.splitlines()]]
pages = [[int(k) for k in j] for j in [i.split(',') for i in pages.splitlines()]]

before = defaultdict(list)
for pair in rules:
    x, y = pair
    before[x].append(y)

def ordered(page):
    seen = []
    for n in page:
        if any(i in seen for i in before[n]):
            return 'wrong'
        seen.append(n)
    return page[int((len(page)-1) / 2)]

def reorder(page):
    new = []
    for n in page:
        for i in before[n]:
            if i in new:
                new.insert(new.index(i), n)
        if n not in new: 
            new.append(n)

    seen = []
    for i in new:
        if i not in seen:
            seen.append(i)

    return seen[int((len(seen)-1) / 2)]

p1, p2 = 0, 0
for p in pages:
    try: p1 += ordered(p)
    except: p2 += reorder(p)
print(p1)
print(p2)