from functools import reduce
from itertools import chain

def sum_of_games(start):
    with open("input.txt") as file:
        text = file.read().split('\n')
    text = [line.split(': ')[1].split('; ') for line in text]
    list_of_lists = []

    for line in text:
        list = []
        for rec in line:
            list.append({x.split(' ')[1]:int(x.split(' ')[0]) for x in rec.split(', ')})
        list_of_lists.append(list)

    return sum(i+1 for i in range(len(list_of_lists)) if all(all(start.get(k,0) >= dic.get(k,0) for k in dic.keys())\
        for dic in list_of_lists[i]))

def sum_of_powersets():
    with open("input.txt") as file:
        text = file.read().split('\n')
    text = [line.split(': ')[1].split('; ') for line in text]
    res = 0
    for line in text:
        single_list = []
        for rec in line:
            single_list.append([ (x.split(' ')[1], int(x.split(' ')[0])) for x in rec.split(', ')])
        min_values = {}
        for color,value in sorted(list(chain(*single_list)),key=lambda x: (x[0],x[1]),reverse=True):
            if color not in min_values:
                min_values[color] = value
        res += reduce(lambda x,y: x*y, min_values.values(),1)
    return res

print(sum_of_games({'red':12,'green':13,'blue':14}))
print(sum_of_powersets())