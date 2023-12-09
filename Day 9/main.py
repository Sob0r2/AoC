def next_in_sequence1():
    file = open("input.txt").read().split('\n')
    arr = [[int(x) for x in f.split(' ')] for f in file]
    res = 0
    for line in arr:
        res += line[-1]
        while True:
            line = list(map(lambda x: x[0]-x[1], zip(line[1:],line)))
            res += line[-1]
            if all(t == 0 for t in line):
                break
    return res

def next_in_sequence2():
    file = open("input.txt").read().split('\n')
    arr = [list(reversed([int(x) for x in f.split(' ')])) for f in file]
    res = 0
    for line in arr:
        diff = line[-1]
        i = 0
        while True:
            line = list(map(lambda x: x[1]-x[0], zip(line[1:],line)))
            if i % 2 == 0: diff -= line[-1]
            else: diff += line[-1]
            if all(t == 0 for t in line): break
            i += 1
        res += diff
    return res

print(next_in_sequence2())
