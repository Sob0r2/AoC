from collections import defaultdict
from functools import reduce
from math import gcd


def create_dict():
    file = open('input.txt').read().split('\n')
    flip_flops = {}
    conjunction = defaultdict(dict)
    rules = {}
    start = []
    for val in file:
        name = val.split('->')[0][:-1]
        rules[name[1:]] = []
        for dest in val.split('->')[1][1:].split(', '):
            rules[name[1:]].append(dest)
        if name.startswith('%'): flip_flops[name[1:]] = 0
        elif name.startswith('&'):
            for val in file:
                key,elems = val.split('->')[0][1:-1], val.split('->')[1][1:]
                for elem in elems.split(', '):
                    if elem == name[1:]: conjunction[name[1:]][key] = 0
        else:
            dests = val.split('->')[1][1:]
            for dest in dests.split(', '): start.append((dest,0))
    return start,flip_flops,conjunction,rules

def ex1(flag,x):
    start,flip_flops,conjuction,rules = create_dict()
    low_sign = 0
    high_sign = 0
    i = 1
    j = 1
    while True:
        stack = []
        for s in start: stack.append(s)
        low_sign += 1
        while stack:
            sym,syg = stack.pop(0)
            if syg == 1: high_sign += 1
            else: low_sign += 1
            if sym in flip_flops:
                if syg == 0:
                    next = 1 if flip_flops[sym] == 0 else 0
                    flip_flops[sym] = next
                    for rule in rules[sym]:
                        if rule in conjuction: conjuction[rule][sym] = next
                        stack.append((rule,next))

            elif sym in conjuction:
                next = 0 if all(val == 1 for val in conjuction[sym].values()) else 1
                for rule in rules[sym]:
                    if flag and sym == x and next == 1: return i
                    if rule in conjuction: conjuction[rule][sym] = next
                    stack.append((rule, next))
        if not flag and j == 1000: return low_sign * high_sign
        i += 1
        j += 1

def lcm(res):
    GCD = reduce(lambda x, y: gcd(x, y), res, res[0])
    return int(reduce(lambda x, y: x * y, res, 1) / GCD)

def ex2():
    return lcm([ex1(1,'xm'),ex1(1,'dr'),ex1(1,'nh'),ex1(1,'tr')])

print(ex1(0,''))
print(ex2())

