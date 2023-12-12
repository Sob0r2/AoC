def prepare_input():
    file = open('input.txt').read().split('\n')
    file = [f.split(' ') for f in file]
    inputs, numbers = [[*f[0]] for f in file], [[int(x) for x in f[1].split(',')] for f in file]
    return inputs,numbers

def ex1():
    inputs,numbers = prepare_input()
    return sum(recursion(i+['.'],n) for i,n in zip(inputs,numbers))

def ex2():
    inputs, numbers = prepare_input()
    return sum(recursion(5*(i+['?']),5*n) for i,n in zip(inputs,numbers))

cache = dict()

def recursion(inputs,numbers):
    if numbers == [] and all([i in '?.' for i in inputs]): return 1
    if (inputs == [] and numbers != []) or (inputs != [] and numbers == []): return 0

    curr = (tuple(inputs),tuple(numbers))
    if curr in cache.keys():
        return cache[curr]

    res = 0
    if inputs[0] in '.?':
        res += recursion(inputs[1:],numbers)
    if inputs[0] in '#?':
        try:
            if all([i in '#?' for i in inputs[:numbers[0]]]):
                try:
                    if inputs[numbers[0]] == '#':
                        return res
                    else:
                        res += recursion(inputs[numbers[0]+1:], numbers[1:])
                except IndexError: pass
        except IndexError: pass
    cache[curr] = res
    return res

print(ex1())
print(ex2())

