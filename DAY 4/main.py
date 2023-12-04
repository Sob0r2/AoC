
def lottery_win():
    with open("DAY 4/input.txt") as f:
        f = f.read().split("\n")
    sum  = 0
    for line in f:
        ctr = 0
        winning,ours = line.split(':')[1].split('|')
        winning = list(filter(lambda x: len(x) >= 1, winning.split(' ')))
        ours = list(filter(lambda x: len(x) >= 1, ours.split(' ')))
        for num in winning:
            if num in ours:
                ctr += 1
        if ctr != 0:
            sum += 2 ** (ctr-1)
    return sum

def sum_of_copies():
    with open("DAY 4/input.txt") as f:
        f = f.read().split("\n")
    dic = {k+1:1 for k in range(len(f))}
    for ind,line in enumerate(f):
        ctr = 0
        winning,ours = line.split(':')[1].split('|')
        winning = list(filter(lambda x: len(x) >= 1, winning.split(' ')))
        ours = list(filter(lambda x: len(x) >= 1, ours.split(' ')))
        for num in winning:
            if num in ours:
                ctr += 1
        for j in range(1,ctr+1):
            try:
                dic[ind+1+j] += dic[ind+1]
            except IndexError:
                pass
    return sum(dic.values())

print(lottery_win())
print(sum_of_copies())