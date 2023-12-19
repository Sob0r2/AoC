from collections import defaultdict, OrderedDict, deque

MIN = 1
MAX = 4000

def workflows():
    rules,inputs = open('input.txt').read().split('\n\n')
    rules = rules.split('\n')
    inputs = inputs.split('\n')
    dic_of_rules = {x.split('{')[0]: x.split('{')[1][:-1] for x in rules}
    final_rules_dic = {}
    for k,v in dic_of_rules.items():
        ins = v.split(',')
        tmp_dict = OrderedDict()
        for i in ins:
            dir = None
            if '<' in i: dir = 'u'
            elif '>' in i: dir = 'd'
            else:
                tmp_dict['f'] = i
                break
            i = i.replace('<','^').replace('>','^')
            s,val,next = i.split('^')[0],int(i.split(':')[0].split('^')[1]),i.split(':')[1]
            if dir == 'u':
                if s in tmp_dict: tmp_dict[s+ '%'] = (MIN,val-1,next)
                else: tmp_dict[s] = (MIN,val-1,next)
            else:
                if s in tmp_dict: tmp_dict[s+'%'] = (val+1,MAX,next)
                else: tmp_dict[s] = (val+1,MAX,next)
        final_rules_dic[k] = tmp_dict
    return inputs,final_rules_dic,dic_of_rules

def ex1():
    inputs,final_rules,_ = workflows()
    res = 0
    for input in inputs:
        x, m, a, s = (int(val.split('=')[1]) for val in input[1:-1].split(','))
        start = 'in'
        while start not in ['R','A']:
            flag = False
            for k,vals in final_rules[start].items():
                try:
                    k = k.split('%')[0]
                except Exception: pass
                if k == 'f':
                    start = vals
                    break
                if vals[0] <= eval(k) <= vals[1]:
                    start = vals[2]
                    flag = True
                    break
                if flag: break
            if start == 'A': res += x+m+a+s
    return res


def new_range(op, n, lo, hi):
  if op=='>':
    lo = max(lo, n+1)
  elif op=='<':
    hi = min(hi, n-1)
  elif op=='>=':
    lo = max(lo, n)
  elif op=='<=':
    hi = min(hi, n)
  else:
    assert False
  return (lo,hi)

def new_ranges(var, op, n, xl,xh,ml,mh,al,ah,sl,sh):
  if var=='x':
    xl,xh = new_range(op, n, xl, xh)
  elif var=='m':
    ml,mh = new_range(op, n, ml, mh)
  elif var=='a':
    al,ah = new_range(op, n, al, ah)
  elif var=='s':
    sl,sh = new_range(op, n, sl, sh)
  return (xl,xh,ml,mh,al,ah,sl,sh)

def ex2():
    _, _, final_results = workflows()
    Q = deque([('in',1,4000,1,4000,1,4000,1,4000)])
    ans = 0
    while Q:
        start,xp,xk,mp,mk,ap,ak,sp,sk = Q.pop()
        if start == 'A':
            ans += (xk-xp+1)*(mk-mp+1)*(ak-ap+1)*(sk-sp+1)
            continue
        elif start == 'R': continue
        else:
            rules = final_results[start]
            for rule in rules.split(','):
                res = rule
                if ':' in rule:
                    cond, res = rule.split(':')
                    var = cond[0]
                    op = cond[1]
                    n = int(cond[2:])
                    Q.append((res, *new_ranges(var,op,n,xp,xk,mp,mk,ap,ak,sp,sk)))
                    xp,xk,mp,mk,ap,ak,sp,sk = new_ranges(var, '<=' if op=='>' else '>=', n, xp, xk, mp, mk, ap, ak,sp, sk)
                else:
                    Q.append((res, xp, xk, mp, mk, ap, ak, sp, sk))
                    break
    return ans


print(ex1())
print(ex2())