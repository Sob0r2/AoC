import numpy as np

dir_to_val = {'left': (0,-1), 'right': (0,1), 'up': (-1,0), 'down': (1,0)}
possible_routes = {('right','/'): 'up', ('left', '/'): 'down', ('down','/'): 'left', ('up','/'): 'right',
                   ('right','\\'): 'down', ('left', '\\'): 'up', ('down','\\'): 'right', ('up','\\'): 'left',
                   ('left','|'): ['up','down'], ('right','|'): ['up','down'],
                   ('up', '-'): ['left','right'], ('down','-'): ['left','right']}

def ex1(x,y,dir):
    file = open('input.txt').read().split('\n')
    mat = np.array([[*line] for line in file])
    mat = np.pad(mat,pad_width=1,constant_values='#')
    visited = set()
    queue = []
    queue.append((dir,(x,y)))
    visited.add(((x,y),dir))
    res = set()
    res.add((x,y))
    while queue:
        dir,tpl = queue.pop(0)
        if (dir,mat[tpl]) in possible_routes.keys():
            new_dir = possible_routes[(dir,mat[tpl])]
            if isinstance(new_dir,str): new_dir = [new_dir]
            for d in new_dir:
                next_ind = (tpl[0] + dir_to_val[d][0], tpl[1] + dir_to_val[d][1])
                if mat[next_ind] != '#':
                    if ((next_ind,d)) not in visited:
                        visited.add((next_ind,d))
                        res.add(next_ind)
                        queue.append((d, next_ind))
        else:
            next_ind = (tpl[0] + dir_to_val[dir][0], tpl[1] + dir_to_val[dir][1])
            if mat[next_ind] != '#':
                if ((next_ind, dir)) not in visited:
                    visited.add((next_ind, dir))
                    res.add(next_ind)
                    queue.append((dir, next_ind))
    return len(res)

def ex2():
    res = 0
    for i in range(1,111):
        tmp = max(ex1(i,1,'right'),ex1(i,1,'up'),ex1(i,1,'down'))
        if tmp > res: res = tmp
    for i in range(1, 111):
        tmp = max(ex1(i, 110, 'left'), ex1(i, 110, 'up'), ex1(i, 110, 'down'))
        if tmp > res: res = tmp
    for i in range(1, 111):
        tmp = max(ex1(1, i, 'right'), ex1(1, i, 'left'), ex1(1, i, 'down'))
        if tmp > res: res = tmp
    for i in range(1, 111):
        tmp = max(ex1(110, i, 'right'), ex1(110, i, 'left'), ex1(110, i, 'up'))
        if tmp > res: res = tmp
    return res

print(ex1(1,1,'right'))
print(ex2())