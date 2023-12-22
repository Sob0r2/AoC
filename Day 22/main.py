import copy
from collections import defaultdict
from itertools import chain


def preprocessing():
    file = open('input.txt').read().split('\n')
    lines = [line.strip().split('~') for line in file]
    bircks = []
    for line in lines:
        tmp = []
        xs, ys, zs = [int(i) for i in line[0].split(',')]
        xe, ye, ze = [int(i) for i in line[1].split(',')]
        if xs == xe and ys == ye and zs == ze:
            tmp.append((xs, ys, zs))
        elif xs != xe:
            for x in range(xs, xe + 1): tmp.append((x, ys, zs))
        elif ys != ye:
            for y in range(ys, ye + 1): tmp.append((xs, y, zs))
        elif zs != ze:
            for z in range(zs, ze + 1): tmp.append((xs, ys, z))
        bircks.append(tmp)

    return bircks

def push_dowm(bricks):
    all_bricks = set(value for brick in bricks for value in brick)
    while True:
        was_change = False
        for i,brick in enumerate(bricks):
            flag = True
            for ele in brick:
                x,y,z = ele
                if z == 1: flag = False
                if (x,y,z-1) in all_bricks and (x,y,z-1) not in brick: flag = False
            if flag:
                was_change = True
                bricks[i] = [(x,y,z-1) for x,y,z in brick]
                for (x,y,z) in brick:
                    all_bricks.discard((x,y,z))
                    all_bricks.add((x,y,z-1))
        if not was_change: break
    return bricks

def prepare_dict(bricks):
    all_bricks = set(value for brick in bricks for value in brick)
    all_bricks_id = {val: id for id, row in enumerate(bricks) for val in row}
    res_dict = defaultdict(list)
    for id, brick in enumerate(bricks):
        for val in brick:
            x, y, z = val
            if (x, y, z + 1) in all_bricks and (x, y, z + 1) not in brick:
                res_dict[id].append(all_bricks_id[(x, y, z + 1)])
    return res_dict

def ex1():
    bricks = push_dowm(preprocessing())
    res_dict = prepare_dict(bricks)
    res = len(bricks) - len(res_dict.keys())
    for k,vals in res_dict.items():
        tmp_dict = copy.deepcopy(res_dict)
        tmp_dict.pop(k)
        flag = True
        for val in vals:
            flattened_data = set(item for sublist in tmp_dict.values() for item in sublist)
            if val not in flattened_data: flag = False
        if flag: res += 1
    return  res

def ex2():
    bricks = push_dowm(preprocessing())
    res_dict = prepare_dict(bricks)
    fall_count = 0
    for k, vals in res_dict.items():
        first = True
        tmp_dict = copy.deepcopy(res_dict)
        tmp_dict.pop(k)
        queue = [k]
        mem = [0 for i in range(len(bricks))]
        while queue:
            act = queue.pop(0)
            mem[act] = 1
            if not first:
                fall_count += 1
                vals = tmp_dict[act]
            for val in vals:
                supporters = [k for k,v in res_dict.items() if any(i == val for i in v)]
                if all(mem[i] == 1for i in supporters):
                    queue.append(val)
                    queue = list(set(queue))
                    first = False
    return fall_count

print(ex1())
print(ex2())