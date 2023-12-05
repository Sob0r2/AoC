from itertools import chain
from concurrent.futures import ThreadPoolExecutor

def map_to_location():
    file = open("input.txt").read().split('\n')
    seeds = file[0].split(' ')[1:]
    mapping_list = []
    tmp = []
    for line in file[3:]:
        if line == '': continue
        if ':' in line:
            mapping_list.append(tmp)
            tmp = []
        else:
            tmp.append(line.split(' '))
    mapping_list.append(tmp)

    for mapping in mapping_list:
        for i,seed in enumerate(seeds):
            seed = int(seed)
            for val in mapping:
                val = [int(v) for v in val]
                if val[1] <= seed < val[1] + val[2]:
                    seeds[i] = seed - val[1] + val[0]
    return(min(seeds))

def map_to_location_2():
    file = open("input.txt").read().split('\n')

    seeds = file[0].split(' ')[1:]

    mapping_list = []
    tmp = []
    for line in file[3:]:
        if line == '': continue
        if ':' in line:
            mapping_list.append(tmp)
            tmp = []
        else:
            tmp.append(line.split(' '))
    mapping_list.append(tmp)

    i = 10000000
    mapping_list = list(reversed(mapping_list))
    while True:
        tmp = i
        for line in mapping_list:
            x = tmp
            for val in line:
                val = [int(v) for v in val]
                if val[0] <= x < val[0]+val[2]:
                    tmp = tmp - val[0] + val[1]
        for seed in zip(seeds[::2],seeds[1::2]):
            seed = [int(v) for v in seed]
            if seed[0] <= tmp < seed[0] + seed[1]:
                return i
        i += 1
        if i % 100000 == 0:
            print(i)

print(map_to_location_2())