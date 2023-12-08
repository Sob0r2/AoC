from functools import reduce
from math import gcd
def puzzle_part1():
    file = open("input.txt").read().strip('\n').split('\n')
    ins = [*file[0]]
    dic = {line.split(' =')[0]:line.split('(')[1].split(')')[0].replace(',','').split(' ') for line in file[2:]}
    start = 'AAA'
    ctr = 0
    while True:
        for i in ins:
            if i == 'L': start = dic[start][0]
            else: start = dic[start][1]
        ctr += 1
        if start == 'ZZZ': break
    return ctr * len(ins)

def puzzle_part2():
    file = open("input.txt").read().strip('\n').split('\n')
    ins = [*file[0]]
    dic = {line.split(' =')[0]:line.split('(')[1].split(')')[0].replace(',','').split(' ') for line in file[2:]}
    start = [x for x in dic.keys() if x[2] == 'A']
    end = [x for x in dic.keys() if x[2] == 'Z']
    res = []
    for s in start:
        ctr = 0
        while True:
            for i in ins:
                if i == 'L': s = dic[s][0]
                else: s = dic[s][1]
            ctr += 1
            if s[2] == 'Z':
                res.append(ctr)
                break
    GCD = reduce(lambda x,y: gcd(x,y),res,res[0])
    return int(reduce(lambda x,y: x * y, res, 1) / GCD) * len(ins)

print(puzzle_part1())
print(puzzle_part2())