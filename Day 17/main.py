import numpy as np
import heapq

dir_to_idx = {'left': [(0,-1),'right'], 'right': [(0,1),'left'], 'up': [(-1,0),'down'],
              'down': [(1,0), 'up']}

def shortest_path(ex):
    file = open('input.txt').read().split('\n')
    mat = np.array([[int(x) for x in l] for l in file])
    visited = {}
    queue = [(0,0,0,-1,-1)]
    while queue:
        val,s,e,dir,steps = heapq.heappop(queue)
        if (s,e,dir,steps) in visited.keys(): continue
        visited[(s,e,dir,steps)] = val
        for d in dir_to_idx.keys():
            new_s = s + dir_to_idx[d][0][0]
            new_e = e + dir_to_idx[d][0][1]
            new_dir = d
            new_steps = 1 if new_dir != dir else steps + 1
            if ex == 1:
                if new_steps > 3 or dir_to_idx[new_dir][1] == dir: continue
            else:
                if new_steps > 10 or dir_to_idx[new_dir][1] == dir or\
                        ((new_dir != dir and steps < 4) and steps != -1): continue
            if 0 <= new_s < mat.shape[0] and 0 <= new_e < mat.shape[1]:
                cost = mat[new_s,new_e]
                heapq.heappush(queue,(val+cost, new_s, new_e, new_dir, new_steps))

    res = 100000000
    for (s,e,dir,steps), val in visited.items():
        if s == mat.shape[0] - 1 and e == mat.shape[1] - 1:
            if val < res: res = val
    return res

print(shortest_path(1))
print(shortest_path(2))