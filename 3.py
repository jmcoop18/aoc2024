def mult(string):
    expressions = [i.split(')') for i in string.split('mul(')]
    t = 0
    for i in expressions[1:]:
        try:
            # evlauate if there are no extra characters & there are multiple numbers
            if (i[0][-1].isnumeric()) and (i[0].count(',') != 0):
                t += eval(i[0].replace(',', '*'))
        except:
            pass
    return t

f = open('3.txt').read()
print(mult(f))

f = [i.split("don't()") for i in f.split('do()')]
p2 = 0
for i in f:
    p2 += mult(i[0])
print(p2)
