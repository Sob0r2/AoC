import numpy as np

directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
pipe_directions = {
    ('L', 'left'): 'up', ('F', 'up'): 'right', ('7', 'right'): 'down',
    ('J', 'down'): 'left', ('F', 'left'): 'down',
    ('7', 'up'): 'left', ('J', 'right'): 'up', ('L', 'down'): 'right',
    ('-', 'left'): 'left', ('-', 'right'): 'right', ('|', 'up'): 'up', ('|', 'down'): 'down'
}
def ex1():
    file_content = open("input.txt").read()
    mat = [list(text) for text in file_content.split('\n')]
    path = dfs(mat)
    return len(path)//2

def ex2():
    file_content = open("input.txt").read()
    mat = [list(text) for text in file_content.split('\n')]
    path = dfs(mat)
    res = set()
    start = None
    act_dir = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (i,j) in path:
                if path[(i,j)][1] == 'up' or pipe_directions[path[(i,j)]] == 'up':
                    act_dir = 'up'
                elif path[(i,j)][1] == 'down' or pipe_directions[path[(i,j)]] == 'down':
                    act_dir = 'down'
                if start is None:
                    start = act_dir
            elif start == act_dir:
                res.add((i,j))
    return len(res)

def dfs(mat):
    sx, sy = np.argwhere(np.array(mat) == 'S')[0]
    path = {}

    for key,val in directions.items():
        if (mat[sx+val[0]][sy+val[1]],key) in pipe_directions.keys():
            start,dir = (sx+val[0],sy+val[1]), key
            break

    path[(start[0], start[1])] = (mat[start[0]][start[1]], dir)
    queue = []
    queue.append((start[0], start[1]))
    curr = (start[0], start[1])
    flag = False

    while curr != start or not flag:
        flag = True
        if curr == (sx,sy): break
        act = (curr[0] + directions[pipe_directions[path[curr]]][0],
               curr[1] + directions[pipe_directions[path[curr]]][1])
        path[act] = (mat[act[0]][act[1]], pipe_directions[path[curr]])
        curr = act

    for p in ['|','-','7','L','F','J']:
        if (p,path[curr][1]) in pipe_directions.keys():
            if pipe_directions[(p,path[curr][1])] == path[start][1]:
                new_tpl = (p, path[curr][1])
                path[curr] = new_tpl
                return path

print(ex1())
print(ex2())