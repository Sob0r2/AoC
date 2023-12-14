import numpy as np

def ex1():
    file = open('input.txt').read().split('\n')
    arr = np.array([[*f] for f in file])
    res = 0
    for col in range(arr.shape[1]):
        cur = 0
        for i,ele in enumerate(arr[:,col]):
            if ele == '#': cur = i+1
            elif ele == 'O':
                res += arr.shape[0] - cur
                cur += 1
    return res

def move_north(arr):
    for col in range(arr.shape[1]):
        cur = 0
        for i,ele in enumerate(arr[:,col]):
            if ele == '#': cur = i+1
            elif ele == 'O':
                if cur != i: arr[cur,col],arr[i,col] = 'O','.'
                cur += 1
    return arr

def move_south(arr):
    for col in range(arr.shape[1]):
        cur = arr.shape[0] - 1
        i = cur
        for ele in reversed(arr[:,col]):
            if ele == '#': cur = i-1
            elif ele == 'O':
                if cur != i: arr[cur,col],arr[i,col] = 'O','.'
                cur -= 1
            i -= 1
    return arr

def move_west(arr):
    for row in range(arr.shape[0]):
        cur = 0
        for i,ele in enumerate(arr[row,:]):
            if ele == '#': cur = i+1
            elif ele == 'O':
                if cur != i: arr[row,cur],arr[row,i] = 'O','.'
                cur += 1
    return arr

def move_east(arr):
    for row in range(arr.shape[0]):
        cur = arr.shape[1] - 1
        i = cur
        for ele in reversed(arr[row,:]):
            if ele == '#': cur = i-1
            elif ele == 'O':
                if cur != i: arr[row,cur],arr[row,i] = 'O','.'
                cur -= 1
            i -= 1
    return arr

def ex2():
    file = open('input.txt').read().split('\n')
    arr = np.array([[*f] for f in file])
    arr_of_hash = []
    start,lenght = 0,0
    for i in range(1000000000):
        h = hash(tuple(tuple(row) for row in arr))
        if h in arr_of_hash:
            start = arr_of_hash.index(h)
            lenght = i - start
            break
        arr_of_hash.append(h)
        arr = move_east(move_south(move_west(move_north(arr))))

    cur = (1000000000-start) % lenght

    arr = np.array([[*f] for f in file])
    for i in range(cur+start):
        arr = move_east(move_south(move_west(move_north(arr))))

    res = 0
    for row in range(arr.shape[0]):
        for col in range(arr.shape[0]):
            if arr[row][col] == 'O':
                res += arr.shape[1] - row
    return res

print(ex1())
print(ex2())