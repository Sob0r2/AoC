import re
from functools import reduce

def sum_of_sentence(file):
    with open(file) as f:
        text = f.read().split('\n')
    text = [replace_letters(i) for i in text]
    num = [re.sub(r'[^0-9]','',i) for i in text]
    return reduce(lambda x,y: x+ int(y[0]+y[-1]),num,0)

def replace_letters(text):
    dic = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
           'nine': '9'}
    for i in dic.keys():
        if i in text:
            text = re.sub(i,i[:2] + dic[i] + i[2:],text)
    return text

print(sum_of_sentence('input.txt'))
