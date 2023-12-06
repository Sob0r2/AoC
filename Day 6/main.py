import math
import re
from functools import reduce

def opp_to_break_record():
    file = open("input.txt").read().split('\n')
    times = re.findall('\d+',file[0],)
    times = [int(t) for t in times]
    dist = re.findall('\d+',file[1])
    dist = [int(d) for d in dist]
    res = []
    for i in range(len(times)):
        delta = (times[i])**2 - 4*dist[i]
        if delta != 0:
            x1 = math.ceil((times[i] - math.sqrt(delta))/2)
            x2 = math.floor((times[i] + math.sqrt(delta))/2)
            x1 = x1 if (times[i] - x1) * x1 > dist[i] else x1 +1
            x2 = x2 if (times[i] - x2) * x2 > dist[i] else x2-1
            res.append(x2-x1+1)
    return reduce(lambda x,y: x*y,res,1)

def sum_record():
    file = open("input.txt").read().split('\n')
    time = re.findall('\d+', file[0], )
    time = int(reduce(lambda x,y: x + y, time))
    dist = re.findall('\d+', file[1])
    dist = int(reduce(lambda x,y: x + y, dist))
    delta = (time) ** 2 - 4 * dist
    if delta != 0:
        x1 = math.ceil((time - math.sqrt(delta)) / 2)
        x2 = math.floor((time + math.sqrt(delta)) / 2)
        x1 = x1 if (time - x1) * x1 > dist else x1 + 1
        x2 = x2 if (time - x2) * x2 > dist else x2 - 1
        return x2-x1+1

print(sum_record())