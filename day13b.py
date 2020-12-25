import sys
from functools import reduce

#sample input
# 939
# 7,13,x,x,59,x,31,19
# you can ignore the first line of the input
def main():
    f = open('day13.txt', 'r') 
    
    f.readline()
    buses = f.readline().strip().split(',')
    
    n = []
    a = []
    #prods = 1

    for idx, val in enumerate(buses):
        if val == 'x':
            continue
        
        val = int(val)

        if idx == 0:
            a.append(0)
            n.append(val)
            continue

        if val == idx:
            a.append(0)
            n.append(val)
        elif val > idx:
            a.append(val-idx)
            n.append(val)
        else:
            a.append(val-(idx%val))
            n.append(val)
    
    print(chinese_remainders(n,a))
    #print(mods)


def chinese_remainders(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def bezut_coeff(a,b, si, ti):
    if a%b == 0:
        return b
    else:
        qi = a//b
        nsi = si[len(si)-2] - qi * si[len(si)-1]
        nti = ti[len(ti)-2] - qi * ti[len(ti)-1]

        si.append(nsi)
        ti.append(nti)

        return bezut_coeff(b,a%b,si,ti)


if __name__ == '__main__':
    main()