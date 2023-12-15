def calc(str):
    res = 0
    for c in str:
        res = ((ord(c) + res)*17) % 256
    return res

def ex1():
    file = open('input.txt').read().strip('\n').split(',')
    res = 0
    for val in file:
        res += calc(val)
    return res

def ex2():
    file = open('input.txt').read().strip('\n').split(',')
    Box = {i: dict() for i in range(256)}
    for num in file:
        if '-' in num:
            res = calc(num[:-1])
            if num[:-1] in Box[res].keys(): del(Box[res][num[:-1]])
        if '=' in num:
            num,val = num.split('=')
            res = calc(num)
            Box[res][num] = val
    res = 0
    for j,dic in enumerate(Box.keys()):
        for i,m in enumerate(Box[dic].keys()):
            res += int(Box[dic][m]) * (i+1) * (j+1)
    return res

print(ex2())