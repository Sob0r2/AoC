from collections import defaultdict
import numpy as np

def find_most_popular_edges():
    file = open('input.txt').read().split('\n')
    nodes = defaultdict(list)
    res_dict = {}
    for line in file:
        key,elems = line.split(': ')
        for ele in elems.split(' '):
            nodes[key].append(ele)
            nodes[ele].append(key)
            res_dict[(key,ele)] = 0
    for i in range(20000):
        start,end = np.random.choice(list(nodes.keys()),2)
        queue = []
        visited = {k: 0 for k in nodes.keys()}
        queue.append((start,[start]))
        visited[start] = 1
        vis = []
        print(i)
        while queue:
            act,vis = queue.pop(0)
            if act == end:
                break
            for next in nodes[act]:
                if visited[next] == 0:
                    visited[next] = 1
                    queue.append((next, vis + [next]))
        for ele1,ele2 in zip(vis,vis[1:]):
            if (ele1,ele2) in res_dict.keys():
                res_dict[(ele1,ele2)] += 1
            else: res_dict[(ele2,ele1)] += 1
    res_dict = sorted(res_dict.items(),reverse=True, key=lambda x: x[1])
    print(res_dict)

def bfs(start,nodes):
    queue = [start]
    visited = {start}
    while queue:
        act = queue.pop(0)
        for ele in nodes[act]:
            if ele not in visited:
                queue.append(ele)
                visited.add(ele)
    return visited

def ex1():
    file = open('input.txt').read().split('\n')
    nodes = defaultdict(list)
    for line in file:
        key,elems = line.split(': ')
        for ele in elems.split(' '):
            if (key == 'szl' and ele == 'kcn') or (key == 'fbd' and ele == 'lzd') or (key == 'ptq' and ele == 'fxn'): continue
            nodes[key].append(ele)
            nodes[ele].append(key)
    vis1 = bfs('ptq',nodes)
    vis2 = bfs('fxn',nodes)
    if vis1 & vis2 == set():
        return len(vis1) * len(vis2)

print(ex1())