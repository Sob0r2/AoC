import numpy as np

def empty_rows_and_cols(arr):
    row = []
    col = []
    for i in range(len(arr)):
        if all([k == '.' for k in arr[i]]): row.append(i)
    for j in range(len(arr[0])):
        if all([k == '.' for k in np.array(arr)[:,j]]): col.append(j)
    return row,col

def create_stack_of_distances(points,arr,ex):
    e_row,e_col = empty_rows_and_cols(arr)
    stack = []
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            x_s,x_l = sorted([points[j][0],points[i][0]])
            if ex == 1: x_cor = x_l-x_s + sum([1 for i in range(x_s,x_l) if i in e_row])
            else: x_cor = x_l - x_s + sum([999999 for i in range(x_s, x_l) if i in e_row])
            y_s,y_l = sorted([points[i][1],points[j][1]])
            if ex == 1: y_cor = y_l-y_s + sum([1 for i in range(y_s,y_l) if i in e_col])
            else: y_cor = y_l-y_s + sum([999999 for i in range(y_s,y_l) if i in e_col])
            stack.append(x_cor+y_cor)
    return stack

def ex1(ex):
    file = open("input.txt").read().split('\n')
    arr = [[*f] for f in file]
    points = [(i,j) for i in range(len(arr)) for j in range(len(arr[0])) if arr[i][j] == '#']
    return sum(create_stack_of_distances(points,arr,ex))

print(ex1(1))
print(ex1(2))