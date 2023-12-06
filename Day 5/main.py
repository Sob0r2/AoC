from itertools import chain
from concurrent.futures import ThreadPoolExecutor

def proccesing():
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
    return seeds,mapping_list
def map_to_location():

    seeds,mapping_list = proccesing()
    for mapping in mapping_list:
        for i,seed in enumerate(seeds):
            seed = int(seed)
            for val in mapping:
                val = [int(v) for v in val]
                if val[1] <= seed < val[1] + val[2]:
                    seeds[i] = seed - val[1] + val[0]
    return(min(seeds))

def map_to_location_2():
    seeds, mapping_list = proccesing()
    seeds = [(int(seed[0]), int(seed[0]) + int(seed[1]) - 1) for seed in zip(seeds[::2], seeds[1::2])]
    mapping_list = [[(int(mapp[0]), int(mapp[1]), int(mapp[1]) + int(mapp[2]) - 1) for mapp in mapping] for mapping in
                    mapping_list]

    for mapping in mapping_list:
        new_res = []
        for (ss, se) in seeds:
            act = []
            prev = []
            for (mm, ms, me) in mapping:
                dif = mm - ms
                st = max(ss, ms)
                lst = min(se, me)
                if st <= lst:
                    act.append((st + dif, lst + dif))
                    prev.append((st, lst))

            if prev:
                prev = sorted(prev, key=lambda x: x[0])
                if prev[0][0] > ss:
                    act.append((ss, prev[0][0] - 1))
                for i in range(len(prev) - 1):
                    if prev[i][1] + 1 != prev[i + 1][0]:
                        act.append((prev[i][1] + 1, prev[i + 1][0] - 1))
                if prev[-1][1] < se:
                    act.append((prev[-1][1] + 1, se))

            else:
                act.append((ss, se))
            new_res.append(act)

        seeds = list(chain(*new_res))


    return min(seeds, key=lambda x: x[0])[0]


print(map_to_location_2())