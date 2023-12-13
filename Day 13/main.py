import copy
import numpy as np
def mirrors(ex):
    file = open('input.txt').read().split('\n\n')
    grid = [[x for x in l.split('\n')] for l in file]
    res = 0
    for mat in grid:
        mat = np.array([[a for a in x] for x in mat])
        if ex == 1:
            rows,cols = checkrows(mat,0,ex),checkcols(mat,0,ex)
            if rows is not None: res += rows * 100
            elif cols is not None: res += cols
        else:
            ans_row,ans_col = checkrows(mat,0,1),checkcols(mat,0,1)
            flag = False
            for i in range(mat.shape[0]):
                if flag: break
                for j in range(mat.shape[1]):
                    if flag: break
                    tmp = copy.deepcopy(mat)
                    tmp[i,j] = '.' if tmp[i,j] == '#' else '#'
                    rows, cols = checkrows(tmp,ans_row,ex), checkcols(tmp,ans_col,ex)
                    if rows is not None:
                        res += rows * 100
                        flag = True
                    elif cols is not None:
                        res += cols
                        flag = True
    return res
def checkrows(mat,ans_row,ex):
    for i in range(mat.shape[0]-1):
        if np.array_equal(mat[i,:],mat[i+1,:]):
            to_boundary = min(i,mat.shape[0]-i-2)
            if all(np.array_equal(mat[i-j-1,:],mat[i+j+2,:]) for j in range(to_boundary)):
              if ex == 1: return i + 1
              if ans_row != i+1: return i+1

def checkcols(mat,ans_col,ex):
    for i in range(mat.shape[1] - 1):
        if np.array_equal(mat[:,i],mat[:,i+1]):
            to_boundary = min(i, mat.shape[1] - i - 2)
            if all(np.array_equal(mat[:,i-j-1],mat[:,i+j+2]) for j in range(to_boundary)):
              if ex == 1: return i + 1
              if ans_col != i+1: return i+1

print(mirrors(1))
print(mirrors(2))