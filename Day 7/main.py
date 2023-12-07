from collections import defaultdict
from collections import Counter

def camel_cards():
    file = open("input.txt").read().strip('\n').split()
    cards = [(x[0],int(x[1])) for x in zip(file[::2],file[1::2])]
    d = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'T': 10, 'J': 1, 'Q': 13, 'K': 14, 'A': 15,}
    cards = [(list(map(lambda x: d[x], [*card[0]])),card[1]) for card in cards]
    cards =  sorted(cards, key=lambda x: (sorted(Counter(x[0]).values(),reverse=True),x[0],x[1]))
    return sum(card[1] * (i+1) for i,card in enumerate(cards))

def camel_cards_jokers():
    file = open("input.txt").read().strip('\n').split()
    cards = [(x[0],int(x[1])) for x in zip(file[::2],file[1::2])]
    d = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'T': 10, 'J': 1, 'Q': 13, 'K': 14, 'A': 15,}
    cards = [(list(map(lambda x: d[x], [*card[0]])),card[1]) for card in cards]
    for i,(card,val) in enumerate(cards):
        filtered_card = list(filter(lambda x: x != 1, [*card]))
        if filtered_card != []:
            ctr = Counter(filtered_card)
            best_pick = sorted(card,key= lambda x:(ctr[x],x),reverse=True)[0]
        else:
            best_pick = 1
        cards[i] = ([(i,i) if i != 1 else (best_pick,i) for i in [*card]],val)
    cards =  sorted(cards, key=lambda x: (sorted(Counter(list(map(lambda y: y[0], x[0]))).values(),reverse=True),
                                          list(map(lambda y: y[1], x[0]))))
    return sum(card[1] * (i+1) for i,card in enumerate(cards))

print(camel_cards_jokers())
