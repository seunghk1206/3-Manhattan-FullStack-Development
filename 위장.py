import math
def solution(clothes):
    answer = 0
    a = 0
    b = 0
    c = 0
    wearing = {}
    for each in clothes:
        try:
            wearing[each[1]] += 1
        except:
            wearing[each[1]] = 1
    print(wearing)
    for val in wearing.values():
        a += val
        if val == 2:
            c += 1
        elif val > 2:
            b += val-1
    answer = math.factorial(a)/(math.factorial(b)) - c
    return answer