from numpy import sign
import z3

def calc_coef(x0,x1,y0,y1):
    a = (y1-y0)/(x1-x0)
    b = y1 - x1*a
    return [a,b,(x0,x1,y0,y1)]

def check_past(x0,x1,y0,y1,x_solve,y_solve):
    flag_x = True if sign(x1-x0) == sign(x_solve-x0) else False
    flag_y = True if sign(y1-y0) == sign(y_solve-y0) else False
    return flag_x and flag_y


def ex1(low,high):
    file = open('input.txt').read().split('\n')
    coef_list = []
    res = 0
    for line in file:
        x0,y0 = [int(x) for x in line.split(' @')[0].split(', ')[:2]]
        x_step,y_step = [int(x) for x in line.split('@ ')[1].split(', ')[:2]]
        x1,y1 = x0+x_step, y0+y_step
        coef_list.append(calc_coef(x0,x1,y0,y1))
    for i in range(0,len(coef_list)):
        for j in range(i+1,len(coef_list)):
            try:
                x = (coef_list[j][1] - coef_list[i][1]) / (coef_list[i][0] - coef_list[j][0])
            except ZeroDivisionError:
                if coef_list[j][1] == coef_list[i][1]: res += 1
                continue
            y = coef_list[i][0]*x + coef_list[i][1]
            if low <= x <= high and low <= y <= high:
                x0,x1,y0,y1 = coef_list[i][2]
                flag_1 = check_past(x0,x1,y0,y1,x,y)
                x0, x1, y0, y1 = coef_list[j][2]
                flag_2 = check_past(x0, x1, y0, y1, x, y)
                if flag_1 and flag_2: res += 1
    return res

def ex2():
    file = open('input.txt').read().split('\n')
    ele = []
    for line in file[:3]:
        x0, y0, z0 = [int(x) for x in line.split(' @')[0].split(', ')]
        x_step, y_step, z_step = [int(x) for x in line.split('@ ')[1].split(', ')]
        ele.append((x0,y0,z0,x_step,y_step,z_step))

    s = z3.Solver()
    res_x,res_y,res_z,res_x_step,res_y_step,res_z_step = z3.Ints('res_x res_y res_z res_x_step res_y_step res_z_step')
    t = [ z3.Int('t_%s' % (i)) for i in range(3)]
    for i,(x0,y0,z0,x_step,y_step,z_step) in enumerate(ele):
        s.add(x0+x_step*t[i] == res_x + res_x_step*t[i])
        s.add(y0 + y_step * t[i] == res_y + res_y_step * t[i])
        s.add(z0 + z_step * t[i] == res_z + res_z_step * t[i])
    s.check()
    m = s.model()
    return int(str(m[res_z])) + int(str(m[res_y])) + int(str(m[res_x]))

print(ex1(200000000000000,400000000000000))
print(ex2())