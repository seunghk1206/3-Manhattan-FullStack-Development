import math
def quadSol():
    inp = input().split('+')
    inpS = input('which solution would you like to seek?(p/n)')
    a = inp[0]
    b = inp[1]
    c = inp[2]
    print(a, b, c)
    ap = int(a.split('x^2')[0])
    bp = int(b.split('x')[0])
    cp = int(c)
    if inpS == 'p':
        return (-bp+(bp**2-4*(ap*cp))**(1/2))/(2*ap)
    elif inpS == 'n':
        return (-bp-(bp**2-4*(ap*cp))**(1/2))/(2*ap)
print(quadSol())