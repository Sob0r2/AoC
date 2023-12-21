import copy
import numpy as np

def get_next(curr,arr,cur_arr):
    up = ((curr[0]-1,curr[1]),cur_arr) if curr[0] - 1 >= 0 else ((arr.shape[0]-1,curr[1]),(cur_arr[0]+1,cur_arr[1]))
    down = ((curr[0]+1,curr[1]),cur_arr) if curr[0] + 1 < arr.shape[0] else ((0,curr[1]),(cur_arr[0]-1,cur_arr[1]))
    left = ((curr[0],curr[1]-1),cur_arr) if curr[1] - 1 >= 0 else ((curr[0],arr.shape[1]-1),(cur_arr[0],cur_arr[1]-1))
    right = ((curr[0],curr[1]+1),cur_arr) if curr[1] + 1 < arr.shape[1] else ((curr[0],0),(cur_arr[0],cur_arr[1]+1))
    return up,down,left,right

def ex(st):
    file = open('input.txt').read().split('\n')
    arr = np.array([[*row] for row in file])
    start = np.where(arr == 'S')
    steps = st
    new_queue = [((start[0][0],start[1][0]),(0,0))]
    for i in range(steps):
        queue = copy.deepcopy(list(set(new_queue)))
        new_queue = []
        while queue:
            curr_idx, curr_arr = queue.pop(0)
            for dir,new_arr in get_next(curr_idx,arr,curr_arr):
                if dir is not None and arr[dir] != '#': new_queue.append((dir,new_arr))
    print(len(set(new_queue)))

ex(64)

# PART 2 Calculate on paper quadratic formula: f(x) = 14669x^2 + 14738x + 3701 for x = 202300

print(14669*202300*202300 + 14738*202300 + 3701)
