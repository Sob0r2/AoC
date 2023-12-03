import re
from functools import reduce
def sum_of_engine():
    with open("input.txt") as f:
        file = f.read().split()
    res = 0
    for i,line in enumerate(file):
        for num in re.finditer(r"\d+",line):
            idx = [(i,num.start() - 1), (i, num.end())] + \
                  [(i-1,j) for j in range(num.start()-1,num.end()+1)] + \
                  [(i+1,j) for j in range(num.start()-1,num.end()+1)]
            check = True if any(file[i[0]][i[1]] != '.' for i in idx if 0 <= i[0] < len(file) and 0 <= i[1] < len([*file[:]])) else False
            if check:
                res += int(num.group())
    return res

def mult_of_gears():
    with open("input.txt") as f:
        file = f.read().split()
    res = 0
    dic = {}
    for i,line in enumerate(file):
        for num in re.finditer(r"\d+", line):
            idx = [(i, num.start() - 1), (i, num.end())] + \
                  [(i - 1, j) for j in range(num.start() - 1, num.end() + 1)] + \
                  [(i + 1, j) for j in range(num.start() - 1, num.end() + 1)]
            stars = [i for i in idx if 0 <= i[0] < len(file) and 0 <= i[1] < len([*file[:]]) and file[i[0]][i[1]] == '*']
            if stars != []:
                for star in stars:
                    dic[star] = dic.get(star,[]) + [int(num.group())]
    return reduce(lambda x,y: x +y[0]*y[1], filter(lambda x: len(x) == 2,dic.values()),0)

print(sum_of_engine())
print(mult_of_gears())