def lottery_win():
    with open("input.txt") as f:
        f = f.read().split("\n")
    res = 0
    for line in f:
        winning,ours = line.split(':')[1].split('|')
        winning = list(filter(lambda x: len(x) >= 1, winning.split(' ')))
        ours = list(filter(lambda x: len(x) >= 1, ours.split(' ')))
        ctr = sum(1 for num in winning if num in ours)
        res += 2 ** (ctr-1) if ctr != 0 else 0
    return res

def sum_of_copies():
    with open("input.txt") as f:
        f = f.read().split("\n")
    dic = {k+1:1 for k in range(len(f))}
    for ind,line in enumerate(f):
        winning,ours = line.split(':')[1].split('|')
        winning = list(filter(lambda x: len(x) >= 1, winning.split(' ')))
        ours = list(filter(lambda x: len(x) >= 1, ours.split(' ')))
        ctr = sum(1 for num in winning if num in ours)
        for j in range(1,ctr+1):
            try:
                dic[ind+1+j] += dic[ind+1]
            except IndexError:
                pass
    return sum(dic.values())

print(lottery_win())
print(sum_of_copies())