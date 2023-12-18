import numpy as np

num_to_dir = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
dir_to_idx = {'L': (0,-1), 'R': (0,1), 'U': (-1,0), 'D': (1,0)}

def count_A(xs,ys):
    xs = np.array(xs,dtype=np.longlong)
    ys = np.array(ys,dtype=np.longlong)
    return 0.5 * np.abs(np.dot(xs,np.roll(ys,1)) - np.dot(ys,np.roll(xs,1)))

def ex1():
    file = open('input.txt').read().split('\n')
    lines = [(i.split(' ')[0], int(i.split(' ')[1])) for i in file]
    return count_lava(lines)

def ex2():
    file = open('input.txt').read().split('\n')
    lines = [(num_to_dir[i.split(' ')[2][-2]], int(i.split(' ')[2][2:-2],16)) for i in file]
    return count_lava(lines)

def count_lava(lines):
    xs = []
    ys = []
    boundary = 0
    st_x, st_y = 0, 0
    for dir, num in lines:
        boundary += num
        xs.append(st_x + dir_to_idx[dir][0] * num)
        ys.append(st_y + dir_to_idx[dir][1] * num)
        st_x += dir_to_idx[dir][0] * num
        st_y += dir_to_idx[dir][1] * num
    return count_A(xs,ys)  + boundary // 2 + 1

print(ex1())
print(ex2())