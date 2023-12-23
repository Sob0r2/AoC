import copy

import numpy as np

dir_to_idx = {">": (0,1), '<': (0,-1), "^": (-1,0), "v": (1,0)}

def make_step(arr,next, visited, flag):
    try:
        if arr[next] == '#': return False
        else:
            if flag: return True
            else:
                if visited[next] == 0: return True
                else: return False
    except IndexError: return False

def ex1():
    file = open('input.txt').read().split('\n')
    arr = np.array([[*row] for row in file])
    visited = np.zeros(arr.shape)
    start = (0,1)
    queue = []
    visited[start] = 1
    queue.append((start,0,visited))
    max_route = 0
    while queue:
        act,dis,visited = queue.pop(0)
        visited = copy.deepcopy(visited)
        if act == (arr.shape[0]-1,arr.shape[1]-2):
            if max_route < dis: max_route = dis
        if arr[act] == '.':
            for dir in [(-1,0),(1,0),(0,1),(0,-1)]:
                next = (act[0]+dir[0],act[1]+dir[1])
                if make_step(arr,next,visited,False):
                    visited[next] = 1
                    queue.append((next,dis+1,visited))
        elif arr[act] in dir_to_idx.keys():
            next = (act[0]+dir_to_idx[arr[act]][0],act[1]+dir_to_idx[arr[act]][1])
            if make_step(arr,next,visited,False):
                visited[next] = 1
                queue.append((next, dis + 1,visited))
    return max_route

def create_list_of_poss(act,arr):
    return [(act[0] + dir[0], act[1] + dir[1]) for dir in [(-1, 0), (1, 0), (0, 1), (0, -1)] if
     make_step(arr, (act[0] + dir[0], act[1] + dir[1]), [], True)]

def create_graph(arr):
    graph = {}
    start = (0,1)
    queue = []
    visited = set()
    queue.append(start)
    while queue:
        act = queue.pop()
        if act in visited: continue
        graph[act] = []
        for next in create_list_of_poss(act,arr):
            l = 1
            prev = act
            pos = next
            isdeath = False
            while True:
                neigh = create_list_of_poss(pos,arr)
                if neigh == [prev] and arr[pos] in '<>^v':
                    isdeath = True
                    break
                if len(neigh) != 2: break
                for n in neigh:
                    if n != prev:
                        l += 1
                        prev = pos
                        pos = n
                        break
            if isdeath: continue
            graph[act].append((pos,l))
            queue.append(pos)
        visited.add(act)
    return graph


def ex2():
    j = 0
    file = open('input.txt').read().split('\n')
    arr = np.array([[*row] for row in file])
    graph = create_graph(arr)
    start = (0,1)
    goal = (arr.shape[0]-1,arr.shape[1]-2)
    queue = []
    queue.append((start,0,{start}))
    max_route = 0
    while queue:
        last,lenght,visited = queue.pop()
        if last == goal:
            if lenght > max_route:
                max_route = lenght
        else:
            for pos,l in graph[last]:
                if pos not in visited:
                    queue.append((pos,lenght+l,visited | {pos}))
    return max_route

print(ex1())
print(ex2())