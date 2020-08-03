import math
def quadSol():
    def root(num, power):
        return num ** 1/power
    try:
        inp = input().split('+')
        a = inp[0]
        ap = int(a.split('x^2')[0])
        if ap == '':
            ap = 1
    except:
        ap = 0
        pass
    try:
        b = inp[1]
        bp = int(b.split('x')[0])
        if bp =='':
            bp = 1
    except:
        bp = 0
        pass
    try:
        c = inp[2]
        cp = int(c)
        print(a, b, c)
    except:
        pass
    print('(x + ', (-bp + root(bp**2-4*(ap*cp), 2))/(2*ap), ')(x + ', (-bp - root(bp**2-4*(ap*cp), 2))/(2*ap), ')')
quadSol()